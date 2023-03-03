
def palin(val):
    global flag
    if len(val) <= 1:
        return flag
    if val[0] == val[-1]:
        palin(val[1:-1])
        return flag
    else:
        flag = False
        return flag

flag = True
print(palin('saippuakivikauppias'.replace(' ', '')))

# the second way
def is_palin(s):
    if len(s) <= 1:
        return True
    else:
        if s[0] == s[-1]:
           return is_palin(s[1:-1])
        else:
            return False 

print(is_palin('а роза упала на лапу азора'.replace(' ', '')))
