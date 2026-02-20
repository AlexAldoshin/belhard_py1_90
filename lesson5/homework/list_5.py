"""
Дан список
['samsung', 'lg', 'xerox', 'bosch']
Удалить элемент с именем 'xerox'
Добавить элемент на 2 место 'indesit'

"""

c = ["samsung", "lg", "xerox", "bosch"]
c.remove("xerox")
c.insert(1, "indesit")
print(c)
