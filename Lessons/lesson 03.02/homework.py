import datetime

now = datetime.datetime.now()
hours = now.hour
minutes = now.minute

answ = input("If you want to input your time press t:\n")

if answ == 't':
    time = input("input your time value in format hh:mm:\n")
    time = time.split(':')
    hours, minutes = time[0], time[1]


units = {
    1: ['одна', 'одной', 'час', 'первого'],
    12: ['двенадцать', 'двенадцати', 'двенадцать', 'двенадцатого'],
    13: ['тринадцать', 'тринадцати', '', ''],
    20: [],
    30: [],
    40: []
}