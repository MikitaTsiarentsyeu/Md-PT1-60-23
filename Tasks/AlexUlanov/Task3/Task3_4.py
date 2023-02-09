def find_Largest(arr):
    Largest = int(arr[0])
    Largest_index = 0
    for i in range(1, len(arr)):
        if int(arr[i]) > Largest:
            Largest = int(arr[i])
            Largest_index = i
    return Largest_index 


def Second_Large(a):
    a=a.split()
    a = list(dict.fromkeys(a))         
    Large_index = find_Largest(a)
    a.pop(Large_index)
    Large_index = find_Largest(a)
    Largest_2=a[Large_index]
    return int(Largest_2)


a = input("Please enter your digits (examle: 3 5 7 4)\n")


print(Second_Large(a))



