str = input("Введите предложение:\n")
st = ""
for i in str:
    if i == i.upper():
       st += i.lower()
    elif i == i.lower():
        st += i.upper()
print(st)        