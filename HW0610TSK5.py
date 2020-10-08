def numb_sum():
    try:
        with open('test4.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел: \n')
            file_obj.writelines(line)
            numb = line.split()

            print(sum(map(int, numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')


numb_sum()
