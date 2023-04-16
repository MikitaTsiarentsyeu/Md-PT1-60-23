
list = [1,2,3,4,5,6]
try:
 print(sum(i for i in list  if not i % 2))
except TypeError:
     print(" Недопустимый тип ввода")
