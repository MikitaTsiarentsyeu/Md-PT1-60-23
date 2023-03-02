def freq(str):
  str_list = str.split()
  frequency = {}

  for word in str_list:
      frequency[word] = frequency.setdefault(word, 0) + 1

  for key, value in frequency.items():
      print(key, ':', value)
 
str = " Опасное сближение набрать высоту набрать высоту опасное сближение "
 
freq(str)
