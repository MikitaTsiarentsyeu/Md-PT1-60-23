def revers(Text):
    res=''
    for i in range(len(Text)-1,-1,-1):
        res+=Text[i]
    return res

text = revers(input("Напиши мне что-нибудь"))
print(text)