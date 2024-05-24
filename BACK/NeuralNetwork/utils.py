import re
import torch
import numpy as np

def sentencer(text:str, num_sen=1, default_sen_len=30):    
    splitted = []
    
    string = ''
    i = 0
    while True:
      if i >= len(text):
        if splitted.count(text) == 0 and len(string) > 5:
          splitted.append(string)
        break

      char = text[i]
      string += char
      
      if char == '.' or char == '!' or char == '?':
      
        if(i < len(text) - 1):
          if text[i + 1] == '?':
            string += text[i + 1]
            i += 1
            
        if(i < len(text) - 2):
          if text[i + 1] == '.' and text[i + 2] == '.':
            string += text[i + 1]
            string += text[i + 2]
            i += 2
        
        if len(string) < default_sen_len:
          i += 1
          continue
        
        splitted.append(string)
        
        if i < len(text) - 1:
          i += 1
        
        string = ''
        
      i += 1
    
    if num_sen == 1:
        return splitted
    
    final_splitted = []
    
    i = 0
    while (i + num_sen) < len(splitted):
        string = ''
        for j in range(num_sen):
            var = splitted[i + j] + ' '
            string += var
            
        final_splitted.append(string)
        i += num_sen
        
    end_string = ''
    for j in range(len(splitted) - i):
        var = splitted[i + j] + ' '
        end_string += var
        
    if end_string != '':
        final_splitted.append(end_string)
        
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
  