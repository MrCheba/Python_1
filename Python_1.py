import json
import numpy as np
import matplotlib.pyplot as plt
import os

A = 0

def f(x):
    return(0.5 + (((np.sin(x**2 - A**2))**2 - 0.5) / (np.abs(1 + 0.001 * (x**2 + A**2)))))

start_x = -10
end_x = 10
step = 0.2

x_values = np.arange(start_x, end_x, step)
y_values = [f(x) for x in x_values]

results_dir = 'results'
if not os.path.exists(results_dir):
    os.makedirs(results_dir)

 

with open(os.path.join(results_dir, 'results.json'), 'w') as file:
    file.write(f'"x": [{", ".join(map(str, x_values))}], \n"y": [{", ".join(map(str, y_values))}]')
        

plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('f(x)')
plt.grid(True)
plt.show()

