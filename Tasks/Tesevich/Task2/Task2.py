import datetime
yn = input("Хотите ввести время вручную? (yes\\no)\n")
if yn.count('yes') == 1:
    ct = input("Введите время в формате hh:mm\n")
else:
    curt = str(datetime.datetime.now())
    ct = curt[11:16]
hh = int(ct[0:2])
mm = int(ct[3:])
h = {'00':'ноль', '01':'один', '02':'два', '03':'три', '04':'четыре', '05':'пять',
'06':'шесть', '07':'семь', '08':'восемь','09':'девять','10':'десять',
'11':'одинадцать','12':'двенадцать','13':'тринадцать','14':'четырнадцать',
'15':'пятнадцать','16':"шеснадцать", '17':'семнадцать','18':'восемнадцать', 
'19':'девятнаднадцать', '20':'двадцать', '21':'двадцать один', '22':'двадцать два',
'23':'двадцать три'}
h1 = {'00':'час','01':'два','02':'три','03':'четыре',
'04':"пять", '05':'шесть','06':'семь', 
'07':'восемь', '08':'девять', '09':'десять', 
'10':'одинадцать','11':'двенадцать',
'12':'час','13':'два','14':'три','15':'четыре',
'16':"пять", '17':'шесть','18':'семь', 
'19':'восемь', '20':'девять', '21':'десять', 
'22':'одинадцать','23':'двенадцать'}
h2 = {'00':'первого','01':'второго','02':'третьего','03':'четвертого',
'04':"пятого", '05':'шестого','06':'седьмого', 
'07':'восьмого', '08':'девятого', '09':'десятого', 
'10':'одинадцатого','11':'двенадцатого',
'12':'первого','13':'второго','14':'третьего','15':'четвертого',
'16':"пятого", '17':'шестого','18':'седьмого', 
'19':'восьмого', '20':'девятого', '21':'десятого', 
'22':'одинадцатого','23':'двенадцатого'}
m1 = {'01':'одна', '02':'две', '03':'три', '04':'четыре', '05':'пять',
'06':'шесть', '07':'семь', '08':'восемь','09':'девять','10':'десять','11':'одинадцать',
'12':'двенадцать','13':'тринадцать','14':'четырнадцать','15':'пятнадцать',
'16':"шеснадцать", '17':'семнадцать','18':'восемнадцать', '19':'девятнаднадцать', 
'20':'двадцать', '21':'двадцать один', '22':'двадцать два',
'23':'двадцать три', '24':'двадцать четыре', '25':'двадцать пять', 
'26':'двадцать шесть', '27':'двадцать семь', '28':"двадцать восемь", 
'29':'двадцать девять', 
'31':"тридцать одна", '32':"тридцать две", "33":"тридцать три", 
"34":"тридцать четыре", "35":'тридцать пять', "36":"тридцать шесть", 
"37":"тридцать семь", "38":"тридцать восемь", '39':"тридцать девять",
"40":'сорок', '41':'сорок одна', '42':'сорок две', '43':'сорок три',
'44':'сорок четыре'}
m2= {'59':'одной', '58':'двух', '57':'трех', '56':'четырех', '55':'пяти',
'54':'шести', '53':'семи', '52':'восеми','51':'девяти','50':'десяти',
'49':'одинадцати','48':'двенадцати','47':'тринадцати','46':'четырнадцати',
'45':'пятнадцати'}

if mm == 00:
    hh = (ct[0:2])
    mm = (ct[3:])
    print (h[hh], "часов ровно")
elif mm < 30:
    hh = (ct[0:2])
    mm = (ct[3:])
    print (m1[mm], "минут", h2[hh])
elif mm == 30:
    hh = (ct[0:2])
    mm = (ct[3:])
    print ("половина", h2[hh])
elif mm > 30 and mm < 45:
    hh = (ct[0:2])
    mm = (ct[3:])
    print (m1[mm], 'минут', h2[hh])
elif mm >= 45:
    hh = (ct[0:2])
    mm = (ct[3:])
    print ("без", m2[mm], 'минут', h2[hh])