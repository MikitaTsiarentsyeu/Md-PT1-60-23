'''Write a function that takes a list of strings as an argument
and returns a new list of strings that are all reversed.'''

def reversed(liste):
    new_list=[]
    for i in liste:
        new_list.append(i[::-1])
    return new_list

#tu=['sgfwe,','wefvspo','094357']
#print(reversed(tu))