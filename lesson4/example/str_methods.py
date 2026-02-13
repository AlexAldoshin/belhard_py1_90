
print("=== ОСНОВНЫЕ МЕТОДЫ СТРОК ===")

s = "  Hello, World!  "

# 1. capitalize() — Первая буква БОЛЬШОЙ, остальное маленькие
print("capitalize():", s.capitalize())  # "  hello, world!  "

# 2. casefold() — Максимально агрессивное приведение к нижнему регистру
print("casefold():", "Straße".casefold())  # "strasse" (ß→ss)

# 3. center(width, fillchar=' ') — По центру
print("center(20):", s.center(20, '*'))  # "**  Hello, World!  **"

# 4. count(sub, start=0, end=len(s)) — Считает вхождения подстроки
print("count('l'):", s.count('l'))  # 3

# 5. encode(encoding='utf-8', errors='strict') — В bytes
print("encode():", s.encode().decode())  # b'  Hello, World!  '

# 6. endswith(suffix, start=0, end=len(s)) — Заканчивается ли?
print("endswith('!'):", s.endswith('!'))  # True

print("\n=== ПРОВЕРКИ ===")

# Проверки (все возвращают True/False)
print("isalpha():", "abc123".isalpha())  # False
print("isdigit():", "123".isdigit())     # True
print("isalnum():", "abc123".isalnum())  # True
print("isspace():", "   ".isspace())     # True
print("islower():", "hello".islower())   # True

print("\n=== ИЗМЕНЕНИЕ РЕГИСТРА ===")
print("lower():", s.lower())      # "  hello, world!  "
print("upper():", s.upper())      # "  HELLO, WORLD!  "
print("title():", s.title())      # "  Hello, World!  "
print("swapcase():", "HeLlO".swapcase())  # "hElLo"

print("\n=== ПОИСК ===")
print("find('World'):", s.find("World"))     # 8 (индекс)
print("rfind('l'):", s.rfind('l'))           # 14 (справа)
print("index('o'):", s.index('o'))           # 4 (ошибка если нет)
print("rindex('l'):", s.rindex('l'))         # 14

print("\n=== ЗАМЕНА ===")
print("replace('l', 'L'):", s.replace('l', 'L'))  # Заменяет ВСЕ
print("removeprefix('  '):", s.removeprefix('  '))  # Python 3.9+
print("removesuffix('!'):", "test!".removesuffix('!'))  # "test"

print("\n=== РАЗДЕЛЕНИЕ ===")
print("split():", "a,b,c".split(','))    # ['a', 'b', 'c']
print("rsplit():", ",a,b,c".rsplit(',', 1))  # [',a,b', 'c']
print("splitlines():", "line1\nline2".splitlines())  # ['line1', 'line2']

print("\n=== СОЕДИНЕНИЕ ===")
print("join():", '-'.join(['a', 'b', 'c']))  # "a-b-c"

print("\n=== ОТРЕЗАНИЕ ===")
print("strip():", s.strip())      # Убирает пробелы с концов
print("lstrip():", s.lstrip())    # Слева
print("rstrip():", s.rstrip())    # Справа

print("\n=== ФОРМАТИРОВАНИЕ ===")
print("zfill(10):", "42".zfill(10))  # "0000000042"
print("format():", "{:.2f}".format(3.14159))  # "3.14"

# 🆕 Python 3.12+: markups
print("\n=== PYTHON 3.12+ ===")
print("removeprefix():", "http://test".removeprefix("http://"))  # "test"
print("removesuffix():", "file.txt".removesuffix(".txt"))         # "file"

print("\n🎯 ГЛАВНЫЕ 10:")
print("1. s.lower() / upper()")
print("2. s.strip() / lstrip() / rstrip()")
print("3. s.split() / s.join()")
print("4. s.replace(old, new)")
print("5. s.find() / s.startswith() / s.endswith()")
print("6. s.count() / s.index()")
