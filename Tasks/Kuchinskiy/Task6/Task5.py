# первый элемент последовательности Фибоначчи принимаем под индексом 1
def fibonacci(n, arg1 = 0, arg2 = 1):
    if n == 1:
        return arg1
    return fibonacci(n - 1, arg1 = arg2, arg2 = arg1 + arg2)

print(fibonacci(6))
