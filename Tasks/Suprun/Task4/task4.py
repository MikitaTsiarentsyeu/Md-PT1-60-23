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

#with open("Tasks/Suprun/Task4/new_text.txt", 'w') as new:
    #while text:
     #   new.write(' '.join([x + '\n' for x in text.split() if len(text) <= n]))
      #  break
new_text = ''
count = 0
for i in text.split():
    count += len(i)
    if count > n:
        new_text += '\n'
        count = len(i)
    elif new_text != '':
        new_text += ' '
        count += 1
    new_text += i
new_text = list(new_text.split('\n'))
max_str = max(new_text)
for i in new_text:
    if len(i) < len(max_str):
        i += ' '


#print(max_str)
with open("Tasks/Suprun/Task4/new_text.txt", 'w') as new:
    new.write('\n'.join(new_text))