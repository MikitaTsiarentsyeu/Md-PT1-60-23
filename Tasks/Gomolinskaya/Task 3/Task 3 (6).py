text = "Пирамида Хеопса"
res = ""
for i in text :
 if i.lower() not in "аеёиоуыэюя":
    res += i
print(res)