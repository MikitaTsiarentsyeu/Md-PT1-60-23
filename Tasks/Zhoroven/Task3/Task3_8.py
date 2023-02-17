user_choise = int(input("Enter number of the elements:\n"))

user_num = []
s = 0
# t = s//len(user_num)

for i in range(1, user_choise + 1):
    element = int(input("Enter the element:\n"))
    user_num.append(element)

for i in user_num:
    s += int(i)

average = s // user_choise


print(user_num)
print(s)
print(f"Average of all elemets in the list is: {average}")
