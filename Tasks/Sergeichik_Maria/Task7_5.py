myDict = dict()

def check(input_func):    
    def output_func(*args):

        if args in myDict:
            print("найден в кэше")
            return myDict[args]
        else:
            print("рассчитан")
            myDict[args] = input_func(*args)
   
        return myDict[args]
    return output_func
 
@check
def sum(a, b):
    return a + b
 
print(sum(10, 20))  
print(sum(10, 20))
print(sum(10, -20)) 