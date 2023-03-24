def div_func(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Cannot divide by zero.Please correct your input value'
    
div_numb = int(input('Input the number divider\n'))
divider = int(input('Input the number you want to divide\n'))

print(div_func(div_numb,divider))