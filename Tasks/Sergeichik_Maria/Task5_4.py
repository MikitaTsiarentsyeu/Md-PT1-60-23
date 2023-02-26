from array import *

def CountHighLow (string):
    
    resultInfo = array('i',[0,0])
    for i in string:
        if i.islower():
            resultInfo[0] += 1
        else:
            resultInfo[1] += 1   
    return resultInfo

string = input("Введите строку:\n")    

result = CountHighLow(string)
print("Количество символов в нижнем регистре:" + str(result[0]))
print("Количество символов в верхнем регистре:" + str(result[1]))
