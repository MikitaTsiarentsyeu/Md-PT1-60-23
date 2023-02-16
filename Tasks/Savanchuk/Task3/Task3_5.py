list = input("Enter a list of strings,separating each with a dot :\n")
list = list.split(".")
for i in list:
    if len(i) > 5:
        print(i)
    