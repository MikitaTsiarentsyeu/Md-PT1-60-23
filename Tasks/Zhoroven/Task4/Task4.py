with open("text.txt", 'r') as f:
    text = f.read()

x = int(input("Enter character number > 35: \n"))

words = text.split()
sentence = ""
text_list = []
lenght = 0

for word in words:
    if lenght + len(word) <= x:
        sentence += word + ' '
        lenght += len(word) + 1
    else:
        text_list.append(sentence.strip())
        sentence = word + " "
        lenght = len(word) + 1
if len(sentence.strip()) == x:
    text_list.append(sentence.strip())
    sentence = ""
    lenght = 0
if sentence:
    text_list.append(sentence.strip())


lines = []
for line in text_list:
    words = line.split()
    if len(words) > 1:
        t_space = x - sum(len(word) for word in words)
        b_space = t_space // (len(words) - 1)
        e_space = t_space % (len(words) - 1)
        f_lines = ""
        for i in range(len(words) - 1):
            f_lines += words[i] + ' ' * (b_space + (1 if i < e_space else 0))
        f_lines += words[-1]
    else:
        f_lines = words[0].ljust(x)
    lines.append(f_lines)
with open("new_text.txt", 'w', encoding='utf-8') as new:

    new.writelines('\n'.join(lines))
