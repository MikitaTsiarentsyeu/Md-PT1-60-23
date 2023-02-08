print("Здравствуй путник, нет времени объяснять и вводи числа")
answer = input()
nombers = []
for i in answer:
    if i.isdigit() and max(answer) != i:
        nombers += i
print("так... посмотрим, вот, что ты ввёл", list(answer),"максимально число", max(answer), "А вот второе по велечине \n"
" число", max(nombers))
