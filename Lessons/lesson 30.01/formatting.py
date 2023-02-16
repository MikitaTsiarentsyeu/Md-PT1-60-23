c, d, r = "cat", "dog", "rat"
# "a cat, a dog and a rat"

s = "a " + c + ", a " + d + " and a " + r
"a cat"
"a cat, a"
"a cat, a dog"
"a cat, a dog and a"
"a cat, a dog and a rat"
print(s)

template = "a {}, a {} and a {}"
print(template.format(c, d, r))

print(f"a {c}, a {d} and a {r}")

import datetime
print(f"current time is {datetime.datetime.now().hour}:{datetime.datetime.now().minute}")

x = 25/4.9
print(f"high {x:.0f}!")