'''Write a function that takes a list of strings as an argument and returns a new list
with all the strings that have a length greater than 5'''

def string_length(liste):
    new_list=[]
    for i in liste:
        if len(i)>5:
            new_list.append(i)
    return new_list

#tu=['sgfwe','wefvspo','094357']
#print(string_length(tu))