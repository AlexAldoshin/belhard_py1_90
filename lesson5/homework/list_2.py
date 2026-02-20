"""
Запросить по очереди у пользователя 5 имен. Добавить все в список.
Отсортировать.
Вывести на экран.
Вывести True при наличии в списке имени 'Вася'
"""

names = []

names.append(input("Введите имя: "))
names.append(input("Введите имя: "))
names.append(input("Введите имя: "))
names.append(input("Введите имя: "))
names.append(input("Введите имя: "))

names.sort()
print(names)

print("Вася" in names)
