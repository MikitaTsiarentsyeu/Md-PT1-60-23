
file = open("D:/Гомолинская/Md-PT1-60-23/Tasks/Gomolinskaya/Task 7/text.txt")
text = file.read()
print(text)
try:
    file = open("D:/Гомолинская/Md-PT1-60-23/Tasks/Gomolinskaya/Task 7/text.txt")
except FileNotFoundError:
    print(f"Файл не существует")
else:
    text = file.read()
    print(text)
finally:
    file.close()

