import json
import numpy as np
import matplotlib.pyplot as plt
import sys
import os

# Убедимся, что файл существует
if not os.path.exists(sys.argv[1]):
    print(f"Файл {sys.argv[1]} не найден")
    sys.exit(1)

# Читаем данные из JSON файла
with open(sys.argv[1], 'r') as file:
    data = json.load(file)

x_values = []
y_values = []

# Извлекаем данные из JSON
for x, y in zip(data['x'], data['y']):
    x_values.append(x)
    y_values.append(y)

# Строим график
graf_from_json = plt.subplot()
plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('y')
graf_from_json.set_xlim((-5, 5))
plt.title('Graph of y = f(x)')

def set_yticks_step():
    if len(sys.argv) > 2:
        if sys.argv[2] == "X":
            step = float(sys.argv[3])
    else:
        step = 1
    plt.xticks(np.arange(-10, 11, step))

set_yticks_step()
plt.show()



