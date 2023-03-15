"""it's just a sandwich-maker without semantic content"""

def bread(func):
    def wrapper():
        func()
        print("bread")
    return wrapper

def ingredients(func):
    n = str(input("Enter what do you want to add to your sandwich seppareted by coma:\n"))
    d = { "tomato":"tomato", "salad":"salad"}
    def wrapper():
        for i in n.split(","):
            if i not in d:
                d[i]=str(i)
                print(d[i])
            else:
                print(d[i])
        func()
    return wrapper

@bread
@ingredients
def sandwich(m = str(input("Enter what kind of meat do you want to add to your sandwich. If you want different kinds of meat write it by coma:\n"))):
    d1 = {"beef":"beef"}
    for i in m.split(","):
        if i not in d1:
            d1[i]=str(i)
            print(d1[i])
        else:
            print(d1[i])
sandwich()