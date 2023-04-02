lst = input().split()

def error(l):
    try:
        l = [int(i) for i in l]
        s = 0 
        for i in l:                  
            if i%2 == 0:
                s += i
        return s
    except (TypeError, ValueError):
        return "Invalid input type"
    
print(error(lst))