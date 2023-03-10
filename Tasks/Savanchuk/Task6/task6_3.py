# Подсчет вхождений.
def occurence_count (s, b):
    if s.find(b) == -1:  #find возвращает -1, если нет совпадений
        return 0
    return 1 + occurence_count(s[s.find(b) + 1:], b) 
s = input("Enter the string:\n").lower()
b = input("Enter character:\n").lower()
print(occurence_count(s,b)) 