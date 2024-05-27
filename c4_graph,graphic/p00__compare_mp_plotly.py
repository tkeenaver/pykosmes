import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

# Matplotlib 예제
plt.plot(x, y, label='sin(x)')
plt.legend()

# Plotly 예제
fig = px.line(x=x, y=y, title='sin(x)')
fig.show()

plt.show()