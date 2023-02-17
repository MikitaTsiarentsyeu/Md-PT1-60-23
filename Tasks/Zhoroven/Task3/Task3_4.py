"""Sorting solution"""

# numbers = input("Enter some numbers:\n")

# numbers_list = list((numbers.split(' ')))
# print(numbers_list)

# numbers_list.sort()
# print(numbers_list[-2])

"""Range solution"""

add_list = []

num_list = int(input("Enter number of the elements in list:\n"))

for i in range(1, num_list + 1):
    elements = int(input("Enter the elements:\n"))
    add_list.append(elements)

add_list.sort()

print(f"Second large element: {add_list[-2]}")
