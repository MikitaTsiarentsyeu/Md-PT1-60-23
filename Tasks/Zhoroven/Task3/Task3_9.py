user_input = input("Enter any words:\n")

for i in range(len(user_input)-1, -1, -1):
    print(user_input[i], end="")
