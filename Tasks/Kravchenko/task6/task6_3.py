s = input('Input a string\n')
char = input('Input a character\n')

def char_accurance(s, i = 0, res = 0):
    
    if len(s) == i:
        return res
    
    if char == s[i]:
        res +=1
    return char_accurance(s, i+1, res)
    
print(char_accurance(s))


    
