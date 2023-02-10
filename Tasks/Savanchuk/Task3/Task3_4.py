#list = (input("Введите числа через пробел:\n"))
#list = list.split(" ")
list = [100, 20, 15, 4, 8, 6]
min = 0
second_min = 0
for i in range(1, len(list)):
    if list[i] <= list[min]:
        min = i
for i in range(len(list)):       
    if list[i] < list[second_min] and list[i] != list[min]: 
        second_min = i
print(second_min, list[second_min])
