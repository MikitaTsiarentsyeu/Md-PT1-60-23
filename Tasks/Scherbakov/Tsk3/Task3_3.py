s = input('Enter the words with a "space":\n')

s2 = s.split(' ')

dict = {}

h = 0

for i in range(len(s2)):
    h += 1
    dict[h] = s2[i]
print(dict)
print('The line contains ' + str(h) + ' words')