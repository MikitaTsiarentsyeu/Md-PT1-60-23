import os

print(os.name)

# sep = "\\" if os.name == "nt" else '/'

print(os.sep)

print(os.sep.join(['level 1', 'level 2', 'level 3']))

path = os.path.join('level 1', 'level 2', 'level 3')
print(path)

initial = os.getcwd()
open("test.txt", 'w')

# os.makedirs(path)
# os.chdir(path)
# print(os.getcwd())
# open("test.txt", 'w')

print(os.listdir())

for item in os.walk(os.getcwd()):
    print(item)

os.chdir(path)
os.remove("test.txt")
os.chdir(initial)
os.removedirs(path)