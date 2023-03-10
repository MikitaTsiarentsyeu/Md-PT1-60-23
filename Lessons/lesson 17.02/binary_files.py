import time
chunk = 1000

with open("test.jpg", 'rb') as r:
    with open("test-copy.jpg", 'wb') as w:
        start = time.time()
        while True:
            part = r.read(chunk)
            if part:
                w.write(part)
            else:
                break
        end = time.time()

print(end - start)