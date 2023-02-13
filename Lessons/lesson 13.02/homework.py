# with open("text.txt", 'r', encoding='utf-8') as f:
#     for line in f:
#         with open("new_text.txt", 'a') as new:
#             new.write(' '.join([x.capitalize() for x in line.split()])+"\n")

with open("text.txt", 'r', encoding='utf-8') as f:
    text = f.read()

with open("new_text.txt", 'w') as new:
        new.write(' '.join([x.capitalize() for x in text.split()])+"\n")