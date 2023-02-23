your_string = input("Input any string:\n")
def strings_list(l):
    l = your_string.split()
    m = []
    for elem in l:
        if len(elem) > 5:
            m.append(elem)
    return m
print(strings_list(your_string))

    