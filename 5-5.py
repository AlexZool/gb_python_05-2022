# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

my_file = open('text5_5', 'w', encoding='utf-8')
line = input('Введите числа через пробел: ')
my_file.write(line)
my_file.close()

my_file = open('text5_5', 'r', encoding='utf-8')
content = my_file.read()
print('Sum:', sum(map(int, content.split())))
my_file.close()
