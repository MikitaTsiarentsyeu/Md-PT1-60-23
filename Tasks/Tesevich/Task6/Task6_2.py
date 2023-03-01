def split_join(args):
    args = args.split(' ')
    args = ''.join(args)
    return args

def palindrom_funk(arg, i = -1, rev_string=[]):
    if i == -(len(arg)+1):
        return
    else:
        rev_string.append(arg[i])
        palindrom_funk (arg,(i  -1))
    rev_string= "".join(rev_string)
    if split_join(rev_string) == split_join(arg):
        return True
    else:
        return False

rev_string = palindrom_funk('ΝΙΨΟΝΑΝΟΜΗΜΑΤΑΜΗΜΟΝΑΝΟΨΙΝ') #забавно что итерпритатор даже греческий алфавит кушает

print(rev_string)