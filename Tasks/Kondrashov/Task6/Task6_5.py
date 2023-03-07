def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(n=int(input('Введи число и узнаешь, чему оно равно в последовательности Фибоначчи:\n'))))