text = input("Введите текст: ").lower()

count = 0
for vowel in 'аеиоуюя':
    count += text.count(vowel)


print(count)
