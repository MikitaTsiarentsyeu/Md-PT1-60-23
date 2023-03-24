import time
def exec_time(func):
    def wrapper(a, b):
        start = time.time()
        res = func(a, b)
        end = time.time() - start    
        with open (r"C:\Users\saha2\OneDrive\Рабочий стол\IT-Academy\Md-PT1-60-23\Tasks\Zheltov\Task7\test.txt", 'w') as f: 
            f.write(f"arguments = {a}, {b} '\n' resultat = {res}  '\n' timing = {end}")
        return res
    return wrapper
@exec_time
def division(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Cannot divide by zero") 
print(division(a = int(input('Enter the first number:\n')),
                b = int(input('Enter the second number:\n'))))       