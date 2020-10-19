rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('test3.txt', 'r') as test_obj:
    for i in test_obj:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)

with open('test3ch.txt', 'w+', encoding='utf-8') as file_obj_2:
    file_obj_2.writelines(new_file)
