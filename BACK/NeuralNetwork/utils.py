import re
import torch
import numpy as np

def sentencer(text:str, sen_num=1, min_segment_len=10):
    puncts = '.!?'
    
    letters = 'абвгдеёзжийклмнопрстуфхцчшщыъьэюя'
    
    abbr = ['г', 'гор', 'в', 'вв', 'кг', 'м', 'мб', 'мин', 'мм', 'р', 'руб', 'с', 'сек', 'стр', 'см', 'тыс', 'т', 'тт', 'ч', 
            'обл', 'о', 'пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс', 'пр', 'ц', 'гб', 'кб', 'ул', 'тов', 'спб', 'пп', 'тд', 'тп']

    splitted = []

    string = ''
    i = 0
    while True:
        if i >= len(text):
            break
        
        char = text[i]
        string += char
        
        if char in puncts:
            end_sentence_flag = True
            
            # Проверка не являеляется ли конец предложения - ?!
            if i < len(text) - 1:
                if text[i + 1] in puncts:
                    next_char = text[i + 1]
                    string += next_char
                    i += 1
                    
                    # Проверка не являеляется ли конец предложения - ...
                    if i < len(text) - 1:
                        if text[i + 1] in puncts:
                            next_char = text[i + 1]
                            string += next_char
                            i += 1
                # Проверка явялется ли знак пунктуации концом предложения
                else:
                    if i < len(text) - 1:
                        # Если после знака пунктуации не идет пробел - значит не конец
                        if text[i + 1] != ' ':
                            end_sentence_flag = False
                        # Проверка не встречается ли где поблизости другие знаки пунктуации
                        if i < len(text) - 2:
                            if text[i + 2] in puncts:
                                end_sentence_flag = False
                        if i < len(text) - 3:
                            if text[i + 3] in puncts:
                                end_sentence_flag = False
                                    
            # Проверка не стоит ли точка перед сокращением
            if i > 0 and end_sentence_flag:
                if char == '.':
                    j = i - 1
                    
                    # Строка для записи сокращения
                    abbr_str = ''
                    abbr_flag = True
                    while True:
                        # Пока не дойдем до конца текста
                        if j > -1:
                            # Или пока не дойдем до конца слова
                            if text[j] != ' ':
                                # Запсиываем в строку
                                if text[j].lower() in letters:
                                    abbr_str += text[j]
                                j -= 1
                            else:
                                break
                        else:
                            break
                    
                    # Развернем строку
                    abbr_str = abbr_str[::-1].lower()

                    # Если строка есть в списке сокращений - это не конец предложения
                    if abbr_str in abbr and abbr_flag:
                        end_sentence_flag = False              
            # Если текст начинается с знака пунктуации - это не конец предложения    
            else:
                end_sentence_flag = False
                                                    
            if end_sentence_flag:
                splitted.append(string)
                string = ''
                i += 1            
            
        i += 1
        
    final_splitted = []
    
    string = ''
    i = 0
    while True:
        if i < len(splitted) - sen_num:
            for j in range(sen_num):
                string += (splitted[i + j] + ' ')
            
            if len(string) >= min_segment_len:
                final_splitted.append(string + ' ')
                string = ''
            else:
                while True:
                    if i < len(splitted) - 1:
                        string += splitted[i + 1]
                        i += 1
                        
                        if len(string) >= min_segment_len:
                            final_splitted.append(string + ' ')
                            string = ''
                            break
                    else:
                        final_splitted.append(string)
                        break
        else:
            while i != len(splitted):
                string += (splitted[i] + ' ')
                i += 1
                
            final_splitted.append(string)
            break
        
        i += sen_num
        
    return final_splitted
    
def remove_duplicates(input_list):
  return list(set(input_list))
    
def remove_punctuation(text):
  return re.sub(r'[^\w\s]', '', text)

def split_words(text):
  return re.findall(r'\w+', remove_punctuation(text))

def only_words(input_list):
  alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
  
  output_list = []
  
  for elem in input_list:
    
    flag = True
    
    for char in elem:
      if char not in alphabet:
        flag = False
        
    if flag:
      output_list.append(elem)
      
  return output_list
    

def find_intersection(list1, list2):
  return set(list1) & set(list2)

def find_profanity(text, dirt, lemmatizer):
  r = find_intersection(split_words(text.lower()), dirt)
  r1 = find_intersection(only_words(lemmatizer.lemmatize(text)), dirt)

  if len(r) == 0 and len(r1) == 0:
    return None
  else:
    return remove_duplicates(list(r) + list(r1))
  
def make_sum_100(array):
  arr_sum = array.sum()
  
  diff = abs(100 - arr_sum)
  
  if arr_sum > 100:
    max_i = np.argmax(array)
    
    new_array = []
    
    for i in range(len(array)):
      if i == max_i:
        new_array.append(array[i] - diff)
      else:
        new_array.append(array[i])
  else:
    min_i = np.argmin(array)
    
    new_array = []
    
    for i in range(len(array)):
      if i == min_i:
        new_array.append(array[i] + diff)
      else:
        new_array.append(array[i])
        
  return np.array(new_array)
    
def get_device():
  if torch.cuda.is_available():
    return 'cuda:0'
  else:
    return 'cpu'
  