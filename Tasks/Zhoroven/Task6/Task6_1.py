def rever_word(word):
    if len(word) == 0:
        return word
    return rever_word(word[1:]) + word[0]


print(rever_word('test'))
