# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

replace_dist = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыра'}

my_file = open('text5_4.txt', 'r', encoding='utf-8')
new_file = open('new_text5_4.txt', 'w', encoding='utf-8')

for line in my_file:
    line = line.split(' - ')
    line[0] = replace_dist[line[0]]
    line = ' - '.join(line)
    new_file.write(line)

my_file.close()
new_file.close()