global_var = "test global value"

def print_global_var():
    print(global_var)

print(__name__)
if __name__ == "__main__":
    for i in range(100):
        print(i)