#4task
lst = 'HomeWorkIsDone'

def count_title(x):
    title = 0
    lower = 0
    for letter in x:
        if (letter.istitle()):
            title+=1
        else:
            lower+=1
    return(title, lower)

print(count_title(lst))
