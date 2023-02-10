
list = input("Enter numbers separated by spaces:\n")
list = list.split()
count = 0
for i in list:
    count += int(i)
print(round(count / len(list)))
        