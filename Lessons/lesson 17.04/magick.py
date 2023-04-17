import random

class Collection:

    def __init__(self, *items) -> None:
        self.__items = []
        if items:
            for item in items:
                self.add(item)

    # def get_items(self): VERY BAD APPROACH, NEVER DO SO
    #     return self.__items

    def add(self, item):
        self.__items.insert(0, item)

    def remove(self, item):
        if item in self.__items:
            self.__items.remove(item)

    def __len__(self):
        return len(self.__items)

    def __str__(self) -> str:
        return f"{Collection.__name__}({','.join([str(x) for x in self.__items])})"

    def __iter__(self):
        self.__iterable_items = list(self.__items)
        random.shuffle(self.__iterable_items)
        self.__iterable_index = 0
        return self
    
    def __next__(self):
        if self.__iterable_index >= len(self.__iterable_items):
            del self.__iterable_index
            del self.__iterable_items
            raise StopIteration
        else:
            item = self.__iterable_items[self.__iterable_index]
            self.__iterable_index += 1 
            return item

    def __add__(self, other):
        if isinstance(other, Collection):
            return Collection(*(list(self)+list(other)))
        else:
            raise TypeError(f"cannot concatenate non-{Collection.__name__} object")


    def __getitem__(self, key):
        try:
            return self.__items[key]
        except IndexError as e:
            self.raise_index_error(e)

    def __setitem__(self, key, value):
        try:
            self.__items[key] = value
        except IndexError as e:
            self.raise_index_error(e)

    def raise_index_error(self, e):
        raise IndexError(str(e).replace(list.__name__, Collection.__name__))


coll = Collection(1,2,3,4,5)
print(coll)
print(Collection(5,4,3,2,1))
print(len(coll))

coll.add(6)
print(coll)
coll.remove(6)
print(coll)

for i in coll:
    print(i)

print(list(coll))

coll2 = Collection(6,7,8,9,10)
print(coll+coll2)

print(coll[1])

coll[1] = 4.0
print(coll[1])