# -*- coding: cp1251 -*-
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LinearSegmentedColormap

# Задаем функцию
def f(x1, x2):
    return (np.sin(3*np.pi*x1)**2 ) + (((x1-1)**2)*abs(1+(np.sin(3*np.pi*x2)**2 ))) + (((x2**2 -1)**2)*abs((1+(np.sin(3*np.pi*x2)**2 ))))
# Генерируем данные
x1 = np.linspace(-3, 3, 100)
x2 = np.linspace(-3, 3, 100)
X1, X2 = np.meshgrid(x1, x2)
Y = f(X1, X2)

# Создаем графики
fig = plt.figure(figsize=(10, 10))




# Поверхность
ax1 = fig.add_subplot(221, projection='3d')
cmap = LinearSegmentedColormap.from_list ('red_blue', ['b', 'w', 'r'], 221)
ax1.plot_surface(X1, X2, Y, color='#11aa55', cmap=cmap)
ax1.set_title('3D поверхность')





# Поверхность сверху
ax2 = fig.add_subplot(222)
cmap = LinearSegmentedColormap.from_list ('red_blue', ['b', 'w', 'r'], 222)
ax2.contourf(X1, X2, Y, color='#11aa55', cmap=cmap)
ax2.set_title('Поверхность "вид сверху"')


#меняем количество точек, для сглаживания графика
x1 = np.linspace(-3, 3, 1000)
x2 = np.linspace(-3, 3, 1000)

# График y = f(x1) при x2 = 1
ax3 = fig.add_subplot(223)
plt.plot(x1, f(x1, 1))
ax3.set_title('График y = f(x1) при x2 = 1')

# График y = f(x2) при x1 = 1
ax4 = fig.add_subplot(224)
plt.plot(x2, f(1, x2))
ax4.set_title('График y = f(x2) при x1 = 1')

plt.tight_layout()
plt.show()
