empty_list = []
numbers_list = int(input('Enter number of elements in list, please:\n'))
for i in range(1, numbers_list + 1):
    element = int(input('Enter the elements: '))
    empty_list.append(element)
    empty_list.sort()
print('The second largest element is:', list_val[-2])