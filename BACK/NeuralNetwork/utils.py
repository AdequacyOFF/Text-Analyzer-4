import re
import torch
import numpy as np

from rusenttokenize import ru_sent_tokenize

def sentencer(text:str, sen_num=1, min_segment_len=10):
  splitted = ru_sent_tokenize(text)
      
  merged_splitted = []
  
  string = ''
  i = 0
  while True:
    if i < len(splitted) - sen_num:
      for j in range(sen_num):
        string += (splitted[i + j] + ' ')
          
      if len(string) >= min_segment_len:
        merged_splitted.append(string + ' ')
        string = ''
      else:
        while True:
          if i < len(splitted) - 1:
            string += splitted[i + 1]
            i += 1
                      
            if len(string) >= min_segment_len:
              merged_splitted.append(string + ' ')
              string = ''
              break
          else:
            merged_splitted.append(string)
            break
    else:
      while i != len(splitted):
        string += (splitted[i] + ' ')
        i += 1
              
      merged_splitted.append(string)
      break
      
    i += sen_num
    
  del splitted
  
  return_splitted = []
    
  for splitted in merged_splitted:
    if len(splitted) > 1:
      return_splitted.append(splitted[:-1])
      
  del merged_splitted
      
  return return_splitted
    
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
