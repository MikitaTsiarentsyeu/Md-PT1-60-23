
class Dog:

    def __init__(self, name, breed, color, vaccine_exp):
        self.name = name
        self.breed = breed
        if breed == "wss":
            self.__color = "white"
        else:
            self.__color = color
        self.vaccine_exp = vaccine_exp
        # self.__vaccinated = vaccinated
        # self.__vaccine_exp = vaccine_exp

    def say_hello(self):
        print(f"hello, my name is {self.name} and I'm {self.__color}")

    def geting_a_new_color(self):
        return self.__color
    
    def get_vaccine_exp(self):
        if self.__vaccinated:
            return self.__vaccine_exp
        else:
            return
        
    def set_vaccine_exp(self, year):
        self.__vaccine_exp = year
        self.__vaccinated = True
    
    vaccine_exp = property(get_vaccine_exp, set_vaccine_exp)

psina = Dog("Zephyrka", "wss", "white", 2024)
# psina.init("Zephyrka", "wss", "white")
psina.say_hello()

dog = Dog("Sharik", "n/a", "black", 2024)
# dog.init("Sharik", "n/a", "black")
dog.say_hello()

# dog.__color = "brown"
# dog.__color
print(dog)
print(dog.vaccine_exp)
dog.vaccine_exp = 2025