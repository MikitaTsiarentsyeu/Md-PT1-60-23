def apply(l, f, i=0):
    if i == len(l):
        return
    f(l[i])
    apply(l, f, i+1)

apply([1,2,3,4,5], print)


def clbck():
    print("I'm a callback")

# import threading

# print("before timer")
# threading.Timer(3, clbck).start()
# print("after timer")

# print("the end")