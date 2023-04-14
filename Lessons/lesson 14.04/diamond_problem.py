
class Food:
    def __init__(self,name,type) -> None:
        self.name=name
        self.type=type

    def __str__(self) -> str:
        return self.name
    
class Animal:
    def eat(self,food:Food):
        print(f"eating {food}")

    def phe(self):
        print("phe...")

class Carnivore(Animal):
    def eat(self, food: Food):
        if food.type == "meat":
            return Animal.eat(self, food)
        else:
            super().phe()

class Herbivore(Animal):
    def eat(self, food: Food):
        if food.type == "plant":
            return Animal.eat(self, food)
        else:
            super().phe()


class Omnivore(Herbivore, Carnivore):
    def eat(self, food: Food):
        if food.type == "meat":
            return Carnivore.eat(self, food)
        elif food.type == "plant":
            return Herbivore.eat(self, food)
        else:
            super().phe()

meat = Food("meat", "meat")
grass = Food("grass", "plant")

tigger = Carnivore()
rabbit = Herbivore()
piglet = Omnivore()

for animal in [tigger, rabbit, piglet]:
    print(type(animal))
    for food in [meat, grass]:
        animal.eat(food)

print(Omnivore.mro())