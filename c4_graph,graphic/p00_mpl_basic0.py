import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.cos(x)
plt.rc('font', family='Hancom Gothic')

plt.plot(x, y)
plt.title('Matplotlib 기본 플롯')
plt.xlabel('x 축')
plt.ylabel('y 축')

y2 = np.sin(x)
plt.plot(x, y2, label='sin(x)', color='r', linestyle='--')
plt.legend()
plt.grid(True)
plt.savefig('matplotlib_plot.png')

plt.show()
