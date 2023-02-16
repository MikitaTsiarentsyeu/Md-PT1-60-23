with open("test.txt", 'w') as f:
    f.write("new text from w mode" + ", ")
    f.write("and another text\n")
    f.writelines(["line 1\n", "line 2\n", "line 3"])

with open("test.txt", 'r') as f:
    for line in f:
        print(line)

    # x = f.readlines()
    # print(x)

    # x = f.readline()
    # print(repr(x))
    # print(f.readline())
    # print(f.readline())
    # print(f.readline())
    # print(f.readline())
    # print(f.readline())

    # print(f.read(10))
    # print(f.read(10))
    # print(f.read(10))
    # print(f.read(10))
    # print(f.read(10))
    # print(f.read(10))

    # print(f.read())
    # f.seek(10)
    # print(repr(f.read()))

with open("test.txt", 'a') as f:
    f.seek(0)
    f.write("\nappended text")

with open("test.txt", 'a+') as f:
    f.seek(0)
    f.write("\nappended text")
    f.seek(0)
    print(f.read())

with open("test.txt", 'r+') as f:
    f.write("new text from r+")
    print(f.read())

with open("test.txt", 'w+') as f:
    f.write("new text from w+")
    f.seek(0)
    f.write("test")
    print(f.read())

