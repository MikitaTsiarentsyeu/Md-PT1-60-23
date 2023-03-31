class Animal:

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def sleep(self, amount):
        print(f"sleeping for the next {amount} seconds")


class Cat(Animal):

    def __init__(self, color):
        self.color = color

    def sleep(self, amount):
        print("I'm cat and I will sleep as long as I want")

    def mrr(self):
        print("mrrrrr")

# c = Cat("Simba", "syberian")
# print(c.breed, c.name)
c = Cat("red")
print(c.color)
c.sleep(600)
c.mrr()

print(isinstance(c, Animal))