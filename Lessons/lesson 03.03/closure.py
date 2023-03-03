def maker(n):
    def action(x):
        return x**n

    return action

sq = maker(2)
print(sq(4))

cube = maker(3)
print(cube(4))

pw = []
for i in range(1, 101):
    pw.append(maker(i))

print([maker(i)(2) for i in range(1, 101)])