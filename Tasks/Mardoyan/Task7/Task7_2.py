def file_func(f):
    try:
        with open(f,'r') as s:
            a = s.read()
        return a
    except FileNotFoundError:
        return 'File not found'

f = input('Input a name your file in format "name.txt"') #I created test.txt for use in the program :)
print(file_func(f))
    