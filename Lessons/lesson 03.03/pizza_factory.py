def prepare():
    print("STARTING A NEW PIZZA")
    print("preparing a base")
    print("adding some sauce")

def add_ingridient(ingr):
    print(f"adding {ingr}")

def grind_cheese():
    print("griding cheese")

def bake(temp, time):
    print(f"baking at {temp} celsius for {time} min")

def done():
    print("boxing")
    print("slicing")
    print("done!")


# def make_pepperoni():
#     prepare()
#     add_ingridient("pepperoni")
#     grind_cheese()
#     bake(200, 5)
#     done()

# def make_double_pepperoni():
#     prepare()
#     add_ingridient("pepperoni")
#     add_ingridient("pepperoni")
#     grind_cheese()
#     bake(200, 5)
#     done()

# def make_shrimp_pizza():
#     prepare()
#     add_ingridient("pepperoni")
#     add_ingridient("shrimp")
#     grind_cheese()
#     bake(175, 7)
#     done()

def pizza_factory(temp, time, *ingrs):
    def factory_method():
        prepare()
        for ingr in ingrs:
            add_ingridient(ingr)
        grind_cheese()
        bake(temp, time)
        done()

    return factory_method

make_pepperoni = pizza_factory(200, 5, "pepperoni")
make_double_pepperoni = pizza_factory(200, 5, "pepperoni", "pepperoni")
make_shrimp_pizza = pizza_factory(175, 7, "pepperoni", "shrimp")

make_double_pepperoni()