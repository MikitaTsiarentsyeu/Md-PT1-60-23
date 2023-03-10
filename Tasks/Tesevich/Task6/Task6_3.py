def count_str(string, symbol,  i = 0, con =0):
    if i == len(string):
        global rez
        rez = con
    else:
        if symbol == string[i]:
            count_str(string, symbol, i+1,con+1)
        else:
            count_str(string, symbol, i+1, con)
    return rez
print(count_str('Какак','а'))
#Какой-то кривой псевдоцикл получился





def count_str(string, symbol,  i = 0, con =0):
     if i == len(string):
        return con
     else:
        if symbol == string[i]:
            return(count_str(string, symbol, i+1,con+1))
        else:
            return(count_str(string, symbol, i+1,con))
print(count_str('Какак','а'))