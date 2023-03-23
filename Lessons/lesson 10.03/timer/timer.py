import time

isRun = False

def start():
    global start_time
    global isRun
    isRun = True
    start_time = time.time()

def finish():
    global isRun
    if isRun:
        isRun = False
        return time.time() - start_time
    else:
        return -1