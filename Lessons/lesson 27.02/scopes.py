test_val = "global value"

def test_scope():
    print(test_val)

def test_scope_2(test_val):
    print(test_val)

def test_scope_3():
    test_val = "test value"
    print(test_val)

test_scope()
test_scope_2("test value")
print(test_val)
test_scope_3()
print(test_val)

l = [1,2,3]

def test_list_append():
    l = 4

test_list_append()
print(l)

def test_global():
    global test_val
    test_val = "new global value"

test_global()
print(test_val)

def outer_outer_func():
    local_value = "local outer value"
    def outer_func():      
        def inner_func():
            nonlocal local_value
            local_value = "local inner value"
            print(local_value)
        inner_func()
        print(local_value)
    outer_func()

outer_outer_func()

def test_global():
    global hgcvbkjlhjgfdzghjkl
    hgcvbkjlhjgfdzghjkl = "hgcvbkjlhjgfdzghjkl"

test_global()
print(hgcvbkjlhjgfdzghjkl)