with open('Workers_salary', 'r') as my_file:
    salary = []
    workers = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            workers.append(i[0])
        salary.append(i[1])
print(f'Оклад меньше 20.000 {workers}, средний оклад {sum(map(int, salary)) / len(salary)}')