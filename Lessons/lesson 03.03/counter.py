def counter_base(n = 0):
    def action():
        nonlocal n
        n += 1
        return n

    return action

from10 = counter_base(10)
from100 = counter_base(100)
print(from10())
print(from100())
print(from10())
print(from100())
