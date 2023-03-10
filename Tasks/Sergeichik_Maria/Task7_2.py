try:
    with open("test.txt", 'r', encoding='utf-8') as f:
        str = f.readlines()
        for i in str:
            print(i)

except  FileNotFoundError:
    print("Несуществующий файл")
