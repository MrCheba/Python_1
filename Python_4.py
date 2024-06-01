# -*- coding: utf-8 -*-
import urllib.request
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import spherical_jn, spherical_yn

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
            D = float(part.split('=')[1].replace(';', ''))  # Удаляем ';' и преобразуем в float
        elif part.startswith('fmin='):
            fmin = float(part.split('=')[1].replace('e9', '').replace(';', '')) * 1e9  # Удаляем 'e9' и ';', преобразуем в float
        elif part.startswith('fmax='):
            fmax = float(part.split('=')[1].replace('e9', '').replace(';', '')) * 1e9  # Удаляем 'e9' и ';', преобразуем в float

# Генерируем диапазон частот
if fmin is not None and fmax is not None:
    freq = range(int(fmin), int(fmax), 100000000)
    print(f"D: {D}, fmin: {fmin}, fmax: {fmax}")
    print(f"Диапазон частот: {list(freq)}")
else:
    print("Не удалось извлечь данные из 9-й строки или данные неполные.")


# Классы для расчета ЭПР и записи результатов
class RCSCalculator:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_rcs(self, frequency):
        wavelength = 3e8 / frequency
        k = 2 * np.pi / wavelength
        n_max = int(np.ceil(k * self.radius) + 10)
        sigma = 0

        for n in range(1, n_max + 1):
            a_n = self.calculate_an(n, k)
            b_n = self.calculate_bn(n, k)
            sigma += ((-1)**n * (n + 0.5) * (b_n - a_n))**2

        sigma = (wavelength**2 / np.pi) * sigma
        return sigma

    def calculate_an(self, n, k):
        kr = k * self.radius
        return spherical_jn(n, kr) / (spherical_jn(n, kr) + 1j * spherical_yn(n, kr))

    def calculate_bn(self, n, k):
        kr = k * self.radius
        return (kr * spherical_jn(n-1, kr) - n * spherical_jn(n, kr)) / (kr * spherical_jn(n-1, kr) - n * spherical_jn(n, kr) + 1j * (kr * spherical_yn(n-1, kr) - n * spherical_yn(n, kr)))

class RCSWriter:
    def __init__(self, filename):
        self.filename = filename

    def write(self, frequencies, rcs_values):
        with open(self.filename, 'w') as f:
            for freq, rcs in zip(frequencies, rcs_values):
                f.write(f"{freq}    {rcs}\n")

# Основная программа для расчета и построения графика
def main():
    radius = D / 2  # Радиус сферы в метрах
    frequencies = list(freq)  # Диапазон частот
    
    calculator = RCSCalculator(radius)
    rcs_values = []

    for frequency in frequencies:
        rcs = calculator.calculate_rcs(frequency)
        rcs_values.append(rcs)

    # Запись результатов в файл
    writer = RCSWriter('rcs_results.txt')
    writer.write(frequencies, rcs_values)

    # Построение графика
    plt.plot(frequencies, rcs_values)
    plt.xlabel('Частота (Гц)')
    plt.ylabel('ЭПР (м^2)')
    plt.title('Зависимость ЭПР от частоты')
    plt.grid(True)
    plt.savefig('rcs_plot.png')
    plt.show()

if __name__ == "__main__":
    main()   
