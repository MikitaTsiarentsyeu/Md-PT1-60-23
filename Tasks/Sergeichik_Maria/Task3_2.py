numbers = (input("enter a number in the format: hhhhh\n"))
sm = 0
for i in numbers:
        if int(i) % 2 == 0:
                sm = sm + int(i)


print(sm)
 
