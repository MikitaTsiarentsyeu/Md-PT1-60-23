strg = input('Enter your string:\n')

def registr(a):
    counter_low = 0
    counter_upp = 0
    for i in a:
        if i.isupper():
            counter_upp += 1
    for i in a: 
        if i.islower():
            counter_low +=1 
    return f'Quantity of uppercase symbols is: {counter_upp}\nQuantity of lowercase symbols is: {counter_low}'
print(registr(strg))