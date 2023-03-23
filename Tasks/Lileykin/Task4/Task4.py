path_to_file = 'test.txt'


def read(text_file: str, line_length: int = 35):
    with open(text_file, 'r', encoding='utf-8') as text:
        line = None
        while line != '':
            line = text.read(line_length)
            yield line

def print_by_width(text_file, line_length):
    for row in read(text_file, line_length):
        print(row)


print_by_width(path_to_file, 35)