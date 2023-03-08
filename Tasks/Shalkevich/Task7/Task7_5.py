Fib = {0:0 , 1:0, 2:1}

def cash(fun):
    def now(*args):
        global Fib
        if args[0] in Fib:
            return Fib[args[0]]
        value =fun(*args)
        Fib[args[0]] = value
        return value
    return now

@cash
def fibonachi(nombers):
    if nombers in Fib:
        return Fib[nombers]
    return fibonachi(nombers - 2) + fibonachi(nombers - 1)
try:
    print(fibonachi(int(input("немного фибоначи?) число.."))))
except ValueError:
    print("Invalid input type")