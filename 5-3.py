# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

my_file = open('text5_3.txt', 'r', encoding="utf-8")
content = my_file.readline()

summary = 0
name = []

for line in content:
    line_split = line.split()
    summary += float(line_split[1])
    if float(line_split[1]) < 20000.00:
        name.append(line_split[0])

my_file.close()

print('Имя: ', ','.join(name))
print('Средняя величина дохода: ', summary / len(content))
