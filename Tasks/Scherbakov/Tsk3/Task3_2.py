import time 

print('Look what I learned in this exercise!')

time.sleep(2)

print('Now My program can return sum of all even numbers from list [1,2,3,5,4,8,6,12,4,8,2,4,8,]')

time.sleep(2)

nswr = input('Do you want to see the result of this programm?(yes/no)\n')

if nswr == 'yes':

    time.sleep(2)

    n = [1,2,3,5,4,8,6,12,4,8,2,4,8,]

    h = 0

    for i in n:
        if i % 2 == 0:
            h += i

    print(h)

else:
    print("If you don't want to see it, I wish you well!)")
