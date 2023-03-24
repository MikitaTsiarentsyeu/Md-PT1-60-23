def sum_all_even(l):
    new_list = [l[i] for i in range(len(l)) if l[i] % 2 == 0]
    return sum(new_list)# + sum_all_even(l[i+1])

try:
    sum_all_even(l)
except NameError:
    print('Invalid input type')
print(sum_all_even([1,2,3,4,5,6,7,8,9,10]))
