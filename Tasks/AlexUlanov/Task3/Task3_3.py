def CountWord(string):
    string=string.split()
    Dict1={}
    for i in range (len(string)):      
        if string[i] in Dict1:
            Dict1[string[i]]+=1
            continue
        Dict1[string[i]]=1  
    return Dict1    

string = input("Please enter your sentence \n")


print(CountWord(string))    

