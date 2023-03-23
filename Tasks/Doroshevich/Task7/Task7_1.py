def div(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "You only need to use numbers"


print(div(14, 0))
