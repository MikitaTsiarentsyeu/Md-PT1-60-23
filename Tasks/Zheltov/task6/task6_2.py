x = str(input("Write your text:\n"))
def polidrom(n):
    if len(n)>1:
        if n[0]==n[-1]:
            polidrom(n[1:-1])
            return
        else:
            print("It's not a palindrome")
            return
    print("It's a palindrome")
    
polidrom(x)