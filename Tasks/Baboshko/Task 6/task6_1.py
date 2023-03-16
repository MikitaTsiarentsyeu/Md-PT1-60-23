def revers(var): 
    if len(var) == 1:
        return var
    else:
        return var[-1] + revers(var[:-1])
    
print(revers('12346789'))

