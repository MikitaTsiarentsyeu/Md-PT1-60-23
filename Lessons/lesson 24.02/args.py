def test_args_keywords(x="not test", y="test"):
    print(f"x:{x}, y:{y}")

test_args_keywords(y="some value")

def sum(*args, sign="+"):
    res = args[0] if len(args) > 0 else 0
    for i in args[1:]:
        if sign == "+":
            res += i
        elif sign == "*":
            res *= i
    return res

print(sum(1,2,3,4,5,sign="*"))

def my_print(*args, sep=' ', end='\n'):
    print(*args, sep=sep, end=end)

my_print(1,2,3,4,5, sep=',', end='.\n')

def my_print(*args, **kwargs):
    print(*args, sep=kwargs['sep'], end=kwargs['end'])

my_print(1,2,3,4,5, sep=',', end='.\n')