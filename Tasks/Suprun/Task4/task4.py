while True:
    n = input("Enter the number of characters in your string(the number must be greater than 35):\n") 
    if not n.isdigit():
        print("Please, use only numeric values")
        continue
    n = int(n)
    if n < 36:
        print("The number must be greater than 35")
        continue
    break
with open("Tasks/Suprun/Task4/text.txt", 'r', encoding='utf-8') as f:
    text = f.read()
with open("Tasks/Suprun/Task4/new_text.txt", 'w', encoding='utf-8') as new:
    new_text = ''
    count = 0
    for i in text.split():
        count += len(i)
        if count >= n:
            new_text += '\n'
            count = len(i)
        elif new_text != '':
            new_text += ' '
            count += 1
        new_text += i
    for i in new_text.split('\n'):
        c = i.count(' ')
        if len(i) < n and c!=0:
            s = (n - len(i)) // c
            p = (n - len(i)) % c
            if s > 0:
                i = i.replace(' ', ' ' + ' ' * s)
            if p > 0:
                i = i.replace(' ' + ' ' * s, ' ' + ' ' * s + ' ', p)
        i = i + '\n'
        new.writelines(i)