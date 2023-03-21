class Engine:

    def __init__(self, power, volume):
        self.__power = power
        self.__volume = volume

    def get_volume(self):
        return self.__volume
    
    def get_power(self):
        return self.__power
    
    power = property(get_power)
    volume = property(get_volume)


class SerialCar:

    def __init__(self, make, model, engine):
        self.__make = make
        self.__model = model
        self.__engine = engine

    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    def get_engine(self):
        return self.__engine
    
    def set_engine(self, engine):
        self.__engine = engine

    make = property(get_make)
    model = property(get_model)
    engine = property(get_engine, set_engine)


class SuperCar:

    def __init__(self, make, model, power, volume):
        self.__make = make
        self.__model = model
        self.__engine = Engine(power, volume)

    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    def get_power(self):
        return self.__engine.power
    
    def get_volume(self):
        return self.__engine.volume

    make = property(get_make)
    model = property(get_model)
    power = property(get_power)
    volume = property(get_volume)


v4 = Engine(100, 2.0)

vw = SerialCar("vw", "golf", v4)

print(vw.make, vw.model, vw.engine.power, vw.engine.volume)

v8 = Engine(200, 4.0)

vw.engine = v8

print(vw.make, vw.model, vw.engine.power, vw.engine.volume)


s = SuperCar("Ferrari", "la Ferrari", 300, 6.3)
print(s.make, s.model, s.power, s.volume)