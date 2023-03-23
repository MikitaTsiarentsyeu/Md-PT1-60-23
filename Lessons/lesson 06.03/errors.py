l = [1,2,3,4,5]

def get(coll, i):
    try:
        return coll[i]
    except IndexError:
        return False
    
def get(coll, i):
    if i <= len(l)-1:
        return coll[i]
    else:
        return False

try:
    print("before")
    test
    print(get([], 100))
    print("after")
except NameError as e:
    print("some variable does not exist")
    print(e)
except IndexError as e:
    print("some index does not exist")
    print(e)
except Exception as e:
    print("something went wrong")
    print(e)


print("the end")