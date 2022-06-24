# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
#
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

my_file = open('text5_6.txt', 'r', encoding='utf-8')
my_dict = {}

for line in my_file:
    line = line.split(':')
    my_dict[line[0]] = line[1]
my_file.close()

for key in my_dict:
    sum = 0
    my_dict[key] = my_dict[key].split()
    for i in range(len(my_dict[key])):
        for char in my_dict[key][i]:
            if char not in '0123456789':
                my_dict[key][i] = my_dict[key][i].replace(char, '')
        try:
            sum += int(my_dict[key][i])
        except:
            continue
    my_dict[key] = sum

print(my_dict)
