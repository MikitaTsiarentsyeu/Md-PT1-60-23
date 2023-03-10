def character_in_string(string, chr):
    if string.find(chr) == -1:
        return 0
    return 1 + character_in_string(string[string.find(chr) + 1:], chr)
print(character_in_string("My first programi", "i"))