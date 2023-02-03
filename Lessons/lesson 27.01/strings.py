x = "test"
another_x = 'test'

print(x == another_x)

test_str = "Hello, it's me"

x = ''' this
    is
    only
    a
    test'''

print(x)
print(repr(x))
print("\thello\n\tit's\n\tme")

"""
test string
"""

s = "my very long string"
print(len(s))
print(s[0], s[1], s[2], s[3], s[4])
print(s[-1], s[-2], s[-3], s[-4])

# print(s[19]) error

print(s[0:4])
print(s[:7])
print(s[:])
print(s[3:-3])

print(s[::-1])