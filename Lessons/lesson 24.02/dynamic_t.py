def times(a, b):
    return a*b

print(times(2, 3))
print(times([2], 3))
print(times('2', 3))

def times_for_int(a:int, b:int) -> int:
    "the function will multiply only int values"
    if isinstance(a, int) and isinstance(b, int):
        return a*b

print(times_for_int('2', 3))

def eq(l1, l2):
    for i in l1:
        if i not in l2:
            return False
    for i in l2:
        if i not in l1:
            return False
    return True

print(eq(['1','2','3'], "2213213213213212"))
print(['1','2','3'] == "2213213213213212")



