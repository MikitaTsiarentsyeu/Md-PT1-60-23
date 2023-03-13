from datetime import datetime

def time(time):
    def now():
        beginning = datetime.now()
        most = time()
        end = datetime.now() - beginning
        with open('text.txt', 'w') as txt:
            x = f'From the beginning = {beginning}, "\n meanings = {most},"\n time of duration = {end}'
            txt.write(x)
        return most
    return now


@time
def dictionary():
    lst = []
    for i in range(10 ** 4):
        if i % 2 == 0:
            lst.append(i)
    return lst

print(dictionary())