import datetime
print(f"current time is {datetime.datetime.now().hour}:{datetime.datetime.now().minute}")
x = input("Enter the time you want in the format: hh:mm\n")
x = x.replace(' ', '')
if len(x) !=5 or x[2] != ":":
    print("enter the correct oder")
    exit()
h_m = x.split(":")
h = int(h_m[0])
m = int(h_m[1])
first_d = { 1 : "одна минута", 2 : "две минуты", 3 : "три минуты", 4 : "четыре минуты", 5 : "пять минут", 6 : "шесть минут", 7: "семь минут",
8 : 'восемь минут', 9:"девять минут", 10:"десять минут", 11:"одинадцать минут", 12:"двенадцать минут", 13:"тренадцать минут",
14:"четырнадцать минут", 15:"пятнадцать минут", 16:"шеснадцать минут", 17:"семнадцать минут", 18:"восемнадцать минут", 19:"девятнадцать минут",
20:"двадцать минут", 21:"двадцать одна минута", 22:"двадцать две минуты", 23:"двадцать три минуты", 24:"двадцать четыре минуты", 
25:"двадцать пять минут", 26:"двадцать шесть минут", 27:"двадцать семь минут", 28:"двадцать восемь минут", 29:"двадцать девять минут", 
30:"половина", 31:"тридцать одна минута", 32:"тридцать две минуты", 33:" тридцать три минуты", 34:"тридцать четыре минуты", 
35:"тридцать пять минут", 36:"тридцать шесть минут", 37:"трицать семь минут", 38:"тридцать восемь минут", 39:"тридцать девять минут", 
40:"без двадцати минут", 41:"без девятнадцати минут", 42:"без восемнадцати минут", 43:"без семнадцати минут", 44:"без шеснадцати минут", 
45:"без пятнадцати", 46:"без четырнадцати минут",47:"без тренадцати минут", 48:"без двенадцати минут", 49:" без одинадцати минут",
50:"без десяти", 51:"без девяти минут", 52:"без восьми минут", 53:"без семи минут", 54:"без шести минут", 55:"без пяти минут",
56:"без четырех минут", 57:"без трех минут", 58:"без двух минут", 59:"без одной минуты"}
second_d = {1:"первого", 2:"второго", 3:"третьего", 4:" четвертого", 5:"пятого", 6:"шестого", 7:"седьмого", 8:"восьмого", 
9:"девятого", 10:"десятого", 11:"одинадцатого", 12:"двенадцатого", 13:"первого"}
serd_d = {1:"один", 2:"два", 3:"три", 4:"черыте", 5:"пять", 6:"шесть", 7:"семь", 8:"восемь", 9:"девять", 10:"десять", 
11:"одинадцать", 12:"двенадцать"}
if m>30:
    print(x+"-"+first_d[m]+" "+second_d[h+1])
elif m<45: 
    print(x+"-"+serd_d[h]+" "+"час"+" "+first_d[m])
print("Классно что это работает :)")
