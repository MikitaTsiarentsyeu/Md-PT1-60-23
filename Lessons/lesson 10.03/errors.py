
try:
    try:
        raise IndexError("The 1 level of IndexError")
        print("the main logic")
    except IndexError:
        raise IndexError("The 2 level of IndexError")
    else:
        print("everything's fine!")
    finally:
        raise IndexError("The 3 level of IndexError")
except IndexError:
    print("the last error")
finally:
    print("finally number 2!")


# with open("test.txt", 'w') as f:
#     f.write("test")

# try:
#     f = open("test.txt", 'w')
#     f.write("test")
# finally:
#     f.close()