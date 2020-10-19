with open('test2.txt', 'r+') as file_obj:
    lines = 0
    letter = 0
    for line in file_obj:
        lines += line.count('\n')
        letter = len(line)-1
        print(f'{letter} Количество символов в строке')
    print(f'Количество строк в файле {lines}')
