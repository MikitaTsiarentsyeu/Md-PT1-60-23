left = input("Введите произвольную строку: \n")
right = ''

for i in range(len(left)-1,-1,-1):
    right += left[i]

print(right)   






