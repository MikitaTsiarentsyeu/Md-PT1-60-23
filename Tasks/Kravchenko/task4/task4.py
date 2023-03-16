import random

n = int(input('Input a number over 35\n'))

with open('text.txt', encoding='utf-8') as file:
    content = file.read().split()

    lengh = 0
    line = []
    new_text = []
    position = 0
    
        
    while position < len(content):
        word = content[position]
        if (n-lengh) > len(word):
            line.append(word)
            lengh += len(word)+1  # '+1'  takes into account spaces following by words
            if position == len(content) - 1:
                line = " ".join(line) 
                new_text.append(line)
                break
            else:
                position += 1   
        
        else: 
            x = n - lengh  # number of remaining spaces
            for _ in range(x):
                random_num = random.randint(1, (len(line)-2))
                line[random_num] = line[random_num] + ' '
                
            line = " ".join(line) + "\n"
            new_text.append(line)
        
            lengh = 0
            line = []    
        

with open('new_file.txt', 'w', encoding='utf-8') as file2:
    file2.writelines(new_text)
          
