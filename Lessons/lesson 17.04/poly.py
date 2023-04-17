class Animal:

    def SaySomething(self):
        print("hello, I'm an animal")

class Dog():

    def SaySomething(self):
        print("Woof")

class Cat():

    def SaySomething(self):
        print("Nyaa")

class Human():
    
    def SaySomething(self):
        print("Hello")

animals = [Animal(), Cat(), Dog(), Human(), 5]
for a in animals:
    a.SaySomething()

print(Cat.__dict__)
c = Cat()
print(c.__dict__)
c.test = "test"
print(c.__dict__)