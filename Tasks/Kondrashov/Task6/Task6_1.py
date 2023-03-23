def recursion(text):
    if len(text) == 1:
        return text
    return text[-1] + recursion(text[:-1])

print(recursion(text=input()))