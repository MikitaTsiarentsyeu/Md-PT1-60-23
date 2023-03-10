def counter_func():
    string = input("Enter a string with lowercase and capital letters and I'll calculate it!!\n")
    print(f'Capital letters: {sum(map(str.isupper,string))}, lowercase: {sum(map(str.islower, string))}')

counter_func()