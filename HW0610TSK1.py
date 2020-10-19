my_file = open('test.txt', 'w')
line = input('Ввод:\n')
while line:
    my_file.writelines(line)
    line = input('Ввод:\n')
    if line == '':
        break


my_file.close()
my_file = open('test.txt', 'r')
content = my_file.readlines()
print(content)
my_file.close()
