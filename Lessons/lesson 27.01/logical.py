
x = -10

if x == 0:
    print("it's zero")
    print("yeah, it's zero")
elif x == 1:
    print("it's one")
elif x == 2:
    print("it's two")
# else:
#     print("idk that number")

if x >= 0:
    if x == 0:
        print("it's zero")
    else:
        flag = True
        print("it's positive")
else:
    print("it's negative")

# print(flag) potential error

print("it's zero") if x == 0 else print("it's positive") if x >= 0 else print("it's negative")

result = "positive" if x > 0 else "negative"
print(result)
print("positive" if x > 0 else "negative")

print("the end")

# print("it's true") if x else print("it's false")

# if x:
#     print("it's true")
# else:
#     print("it's false")