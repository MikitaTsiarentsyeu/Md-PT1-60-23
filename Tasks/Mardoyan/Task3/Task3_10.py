print('Hello!I can return the largest prime number in your list.')
x = input('Input you list of numbers(Throught "space")\n')
prime_list = []
max = 0
x = x.split(' ')
for i in x:
    if (int(i) % 2 != 0 and int(i) % 3 != 0) or ( int(i) == 2 or int(i) == 3):
        prime_list.append(i)
for i in prime_list:
    if int(i) > max:
        max = int(i)
print(max)
