c = 0
def count_func(n,a):
    global c         #Знаю,что глобал лучше не юзать,но не нашел выхода другого.Видел в занятии про nonlocal,но там было 2 функции
    if len(n) == 1:
        if n == a:
            c += 1
            return c
        else:
            return c
    else:
        if n[0] == a:
            c += 1
        return count_func(n[1:],a)
x = input('Input string')
d = input('Input symbol')
print(count_func(x.lower(),d.lower()))
