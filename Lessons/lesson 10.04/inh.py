class FlyingAnimal:

    def fly(self):
        print("mum, look, I'm flying!")

class RunningAnimal:

    def run(self):
        print("I'm running")

class SwimmingAnimal:

    def swim(self):
        print("I'm swimming")


class Duck(FlyingAnimal, RunningAnimal, SwimmingAnimal): pass


class Zero:

    def test(self):
        print("test from Zero")


class A(Zero):

    def test(self):
        super().test()
        print("test from A")

class B(Zero):

    def test(self):
        super().test()
        print("test from B")

class C(B, A):

    def test(self):
        super().test()
        print("test from C")

c = C()
c.test()

print(C.__mro__)