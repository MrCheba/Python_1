import json
import numpy as np
import matplotlib.pyplot as plt
import os

A = 0

def f(x):
    return(0.5 + (((np.sin(x**2 - A**2))**2 - 0.5) / (np.abs(1 + 0.001 * (x**2 + A**2)))))

start_x = -5
end_x = 5
step = 0.2

x_values = np.arange(start_x, end_x, step)
y_values = [f(x) for x in x_values]



# Строим график
plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('f(x)')

def set_yticks_step():
    if(len(sys.argv) > 2):
        if ((sys.argv[2]) == "Y"):
            step = float(sys.argv[3])
    else:
        step = 1
    plt.yticks(np.arange(min(y_values), max(y_values)+1, step))


plt.grid(True)
plt.show()




