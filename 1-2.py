# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите
# в формате чч:мм:сс. Используйте форматирование строк.

a = int(input('Введите секунды: '))
chas = a // 3600 % 24
min = a // 60 % 60
sec = a % 60
print(chas // 10, chas % 10, ':', min // 10, min % 10, ':', sec // 10, sec % 10, sep='')
