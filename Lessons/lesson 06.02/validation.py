while True:
    time = input("Input your time in format 'hh:mm':\n")

    if len(time) != 5:
        print("Incorrect length of the time token, please try again")
        continue

    if time[2] != ":":
        print("Incorrect time token format, please try again")
        continue

    h, m = time.split(':')

    if not h.isdigit() or not m.isdigit():
        print("please use onlu numeric values")
        continue

    h, m = int(h), int(m)

    if h < 0 or h > 23:
        print("incorrect hours value, please try again")
        continue

    if m < 0 or m > 59:
        print("incorrect minutes value, please try again")
        continue

    break

print("the main logic goes here")