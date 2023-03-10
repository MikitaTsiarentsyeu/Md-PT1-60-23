import json

x = int(input("Enter your fisrt number fo divide\n"))
y = int(input("Enter your second number fo divide(denominator)\n"))

def divide (x, y):
    try:
        return x/y
    except:
        print("Cannot divide by zero")
        return False

def log(func):
    def wrapper():

           
        with open ("cash.json", "a", encoding="utf-8") as f:            # Создали пустой файл JSON если его не было   
            pass

        with open ("cash.json", "r", encoding="utf-8") as m:           
            buf = []
            try:    

                buf = json.load(m)        # Прочитали в буфер 
                
                for i in range(len(buf)):
                   
                    if buf[i]["x"] == x and buf[i]["y"] == y:
                        print("Найдено совпадение ключей\nРезультат:", buf[i]["z"])
                        return buf[i]["z"]
                    elif i == len(buf)-1:
                        raise ValueError

            except ValueError:
                print("не Найдено совпадений ключей")
                z = func(x, y)
                keys = ["x", "y", "z"]
                data = x,y,z       
                Dict1 = {}

                for i in range(len(keys)):
                    Dict1[keys[i]] = data[i]

                buf.append(Dict1)

                with open("cash.json", "w") as k: 
                    pass

                with open ("cash.json", "a", encoding="utf-8") as f: 
                    
                    json.dump(buf, f)                     # Записали в файл обновленные данные
                    print(buf)
           
    return wrapper

loG = log(divide)
loG()

