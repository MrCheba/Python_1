
# -*- coding: utf-8 -*-
import urllib.request

# Задаем URL для текстового файла
url = 'https://jenyay.net/uploads/Student/Modelling/task_rcs_01.txt'

# Читаем данные из URL
with urllib.request.urlopen(url) as response:
    dataread = response.read().decode('utf-8')

# Инициализируем переменные
D = None
fmin = None
fmax = None

# Получаем все строки из файла
lines = dataread.splitlines()

# Проверяем, есть ли хотя бы 9 строк в файле
if len(lines) >= 9:
    # Извлекаем 9-ю строку (индекс 8, так как нумерация с нуля)
    line = lines[8]
    
    # Извлекаем необходимые атрибуты из строки
    parts = line.split()
    for part in parts:
        if part.startswith('D='):
            D = float(part.split('=')[1])  # Берем вторую часть после '=' и преобразуем в float
        elif part.startswith('fmin='):
            fmin = float(part.split('=')[1].replace('e9', '')) * 1e9  # Удаляем 'e9' и преобразуем в float
        elif part.startswith('fmax='):
            fmax = float(part.split('=')[1].replace('e9', '')) * 1e9  # Удаляем 'e9' и преобразуем в float

# Генерируем диапазон частот
if fmin is not None and fmax is not None:
    freq = range(int(fmin), int(fmax), 100000000)
    print(f"D: {D}, fmin: {fmin}, fmax: {fmax}")
    print(f"Диапазон частот: {list(freq)}")
else:
    print("Не удалось извлечь данные из 9-й строки или данные неполные.")