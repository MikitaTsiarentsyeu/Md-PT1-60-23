s = input()
def reverse_string(s):
    
    if len(s) == 1:
        return s[0]
    symbol = s[0]
    return reverse_string(s[1::]) + symbol

print(reverse_string(s))
    