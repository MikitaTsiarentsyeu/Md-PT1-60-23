
def limited_lenght_words(words):
    result = []
    for word in words:
        if len(word) >= 5:
            result.append(word)
    return print(result)


limited_lenght_words(
    words=['if', 'limited', 'lenght', 'fivee',  'greater', 'than', 'five', 'or', 'no'])
