import datetime

d = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    21: 'twenty-one',
    22: 'twenty-two',
    23: 'twenty-three',
    24: 'twenty-four',
    25: 'twenty-five',
    26: 'twenty-six',
    27: 'twenty-seven',
    28: 'twenty-eight',
    29: 'twenty-nine',
    30: 'half ',
    31: 'thirty-one',
    32: 'thirty-two',
    33: 'thirty-three',
    34: 'thirty-four',
    35: 'thirty-five',
    36: 'thirty-six',
    37: 'thirty-seven',
    38: 'thirty-eight',
    39: 'thirty-nine',
    40: 'forty',
    41: 'forty-one',
    42: 'forty-two',
    43: 'forty-three',
    44: 'forty-four'
}

d_h = {
    1: 'of the first',
    2: 'of the second',
    3: 'of the third',
    4: 'past four',
    5: 'past five',
    6: 'past six',
    7: 'past seven',
    8: 'past eight',
    9: 'past nine',
    10: 'past ten',
    11: 'past eleven',
    12: 'past twelve',
    13: 'of the first',
    14: 'of the second',
    15: 'of the third',
    16: 'past four',
    17: 'past five',
    18: 'past six',
    19: 'past seven',
    20: 'past eight',
    21: 'past nine',
    22: 'past ten',
    23: 'past eleven',
    24: 'past twelve',
}
time_qstn= input('Do you want to know the current time?(yes/no)\n')

if time_qstn == 'yes':
    h = datetime.datetime.now().hour
    m = datetime.datetime.now().minute
    if m == int(00): 
        print(d.get(m) + ' hours exactly')
    elif m ==int(30):
        print(d.get(m) + d_h.get(h + 1))
    elif m > int(30) and m < int(45):
            print(d.get(m) + ' minutes ' + d_h.get(h + 1))
    else:
        print(d.get(m) + ' minutes ' + d_h.get(h + 1))

elif time_qstn == 'no':
    time_qstn2 = input('Would you like to give your time?(yes/no)\n')
    
    if time_qstn2 == 'no':
        print('Have a good day!')
    elif time_qstn2 == 'yes':
        hrs_mn = input('Enter the current time in format hh:mm\n')
        hrs_mn = hrs_mn.split(':')
        hrs = int(hrs_mn [0])
        mn = int(hrs_mn [1])
    
        if mn == int(00) and hrs >= int(13):
            print(d.get(hrs - 12) + ' hours exactly')
        elif mn == int(00) and hrs <= int(12):
            print(d.get(hrs) + ' hours exactly')

        elif mn < int(30):
            print(d.get(mn) + ' minutes ' + d_h.get(hrs + 1))
    
        elif mn == int(30):
            print(d.get(mn) + d_h.get(hrs + 1))

        elif mn > int(30) and mn < int(45):
            print(d.get(mn) + ' minutes ' + d_h.get(hrs + 1))
 
        elif mn >= int(45) and hrs <= 12:
            print(d.get(60 - mn)  + ' minutes past ' + d.get(hrs + 1))
        elif mn >= int(45) and hrs >= 13:
            print(d.get(60 - mn)  + ' minutes past ' + d.get(hrs - 11))

        else:
            print('Have a good day!')
    else:
        print('Have a good day!')
else:
    print('Have a good day!')