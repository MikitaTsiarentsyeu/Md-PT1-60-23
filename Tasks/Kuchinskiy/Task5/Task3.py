def len_list(s):
    new_s = [s for s in s if len(s) > 5]
    return(new_s)


print(len_list(['test', 'qwerty','asdf','zxcvbnm']))