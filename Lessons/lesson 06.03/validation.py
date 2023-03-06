while True:
    t = input("Input your value in format hh:mm\n")
    try:
        h, m = t.split(':')
        h, m = int(h), int(m)
        if h > 23:
            raise RuntimeError("the hours value was too big")
        if m > 59:
            raise RuntimeError("the minutes value was too big")

        break
    except ValueError:
        print("Incorrect input, please try again")
        continue
    except RuntimeError as e:
        print(e)
        continue

