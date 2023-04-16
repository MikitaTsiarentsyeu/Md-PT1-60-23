def fibonacci(s):
    if (s <= 1):
        return s
    else:
        return (fibonacci(s-1) + fibonacci(s-2))
s = int(input("Введите длинну ряда:"))

print("Последовательность Фибоначчи:")

for i in range(s):
    print(fibonacci(i))
    

