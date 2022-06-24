# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

my_file = open('text5_2.txt', 'r')

content = my_file.readlines()
print('Строк: ', len(content))
for i in range(len(content)):
    print('Строк: ', {i+1}, 'Слов в строке: ', {len(content[i].split())})

my_file.close()
