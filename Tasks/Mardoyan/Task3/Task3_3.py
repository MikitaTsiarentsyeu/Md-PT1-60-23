print('Hello!I can return a dictionary with the count of each word in your string.')
x = input('Input you string(Throught "space")\n')
key = 0
value = ''
dictionary = {}
x = x.split(' ')
for i in x:
    key +=1
    value = i
    dictionary.update({key : value})
print(dictionary)
