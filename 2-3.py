# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

number = int(input("Введите номер месеца: "))
if number <= 12 and number >= 1:
    month_dict = {1: 'Январь',
                  2: 'Февраль',
                  3: 'Март',
                  4: 'Апрель',
                  5: 'Май',
                  6: 'Июнь',
                  7: 'Июль',
                  8: 'Август',
                  9: 'Сентябрь',
                  10: 'Октабрь',
                  11: 'Ноябрь',
                  12: 'Декабрь'}

    month_list = [['зиме', 12, 1, 2], ['весне', 3, 4, 5], ['лету', 6, 7, 8], ['осени', 9, 10, 11]]
    if number in range(1, 13):
        for i, el in enumerate(month_list):
            if number in el[1:4]:
                print(f'')
                break
    else:
        print('Введен некорректный номер месяца!')
print(f"Месец {month_dict[number]} относится к {el[0]}")