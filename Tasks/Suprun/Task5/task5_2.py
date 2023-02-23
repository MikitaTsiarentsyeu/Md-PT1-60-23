your_string = input("Input any string in order to reverse it:\n")
def reversed_string(strings):
    strings = your_string.split()
    return [i[::-1] for i in strings]
print(reversed_string(your_string))