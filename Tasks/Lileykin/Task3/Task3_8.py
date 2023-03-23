def list_avrg(lst):
    l = len(lst)
    suma = 0
    for i in lst:
        suma += i
    return suma / l

values=input("Enter a list of numbers separated by a space\n")
values = values.split()

for i in range(len(values)):
    values[i] = int(values[i])

avrg = list_avrg(values)
print("Average number:")
print(round(avrg, 2))