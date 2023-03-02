def reverse (strings):
    
    res = ''

    for i in range(len(strings)-1,-1,-1):
            res += strings[i]

         
    return res

n = reverse(input("Введите произвольную строку:\n"))    
print(n)