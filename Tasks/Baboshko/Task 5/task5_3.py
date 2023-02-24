def new_list_5(list):
    return [i for i in list if len(i) > 5]
print(new_list_5(input().split()))