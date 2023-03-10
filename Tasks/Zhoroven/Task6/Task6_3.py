def counter(text, character):
    if len(text) == 0:
        return 0
    if text[0] == character:
        return 1 + counter(text[1:],  character)
    return counter(text[1:],  character)


text = 'Paloroid'
character = 'o'
count = counter(text, character)

print(f'Character "{character}" is {count}')
