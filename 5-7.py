# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта: [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

import json

sum =0
profit_counter = 0
firm_dict = {}

with open('text5_7.txt', 'r') as my_file:
    for line in my_file:
        firm_name, firm_type, firm_profit, firm_losses = line.split()
        firm_profit = int(firm_profit)
        firm_losses = int(firm_losses)
        firm_dict[firm_name] = abs(firm_profit-firm_losses)
        if firm_losses < firm_profit:
            sum += (firm_profit-firm_losses)
            profit_counter += 1
profit_dict = {'profit': sum/profit_counter}
my_list = [firm_dict, profit_dict]
print(my_list)

with open('text5_7.json', 'w') as my_file:
    json.dump(my_list, my_file)
