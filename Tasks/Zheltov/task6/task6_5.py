def valyme(n):
    if n in (1, 2):
        return 1
    return valyme(n - 1) + valyme(n - 2)
print(valyme(4))