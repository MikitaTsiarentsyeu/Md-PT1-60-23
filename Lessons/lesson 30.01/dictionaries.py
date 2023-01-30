d = {}
print(type(d), d)

d = {"one":1, "two":2, "three":3}
print(d)

print(d["one"], d["two"])

d['new key'] = "new value"
print(d)

d["one"] = 1.0
d["one"] = "1"
del d["new key"]
print(d)