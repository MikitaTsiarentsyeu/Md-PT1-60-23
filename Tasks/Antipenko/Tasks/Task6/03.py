'''3. Write a recursive function to count the number of occurrences of a given character in a string.'''

def check(string, ch):
    if not string:
        return 0
    elif string[0] == ch:
        return 1 + check(string[1:], ch)
    else:
        return check(string[1:], ch)
string = input("Enter the sentence:\n")
ch = input("Enter the character:\n")
print("Number of occurrences:\t")
print(check(string, ch))