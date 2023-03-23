string = int(input("Enter how many elements will be included in our programm:\n "))
list = []
for i in range(0, string):
    element = int(input("Enter an element:\n "))
    list.append(element)
average_meaning = sum(list) / string
print("The average meaning of all your elements are:",round(average_meaning, 2))