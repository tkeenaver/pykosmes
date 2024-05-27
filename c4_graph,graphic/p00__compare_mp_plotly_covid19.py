import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import pandas as pd

data = pd.read_csv('data/owid-covid-data.csv')
plt.plot(data['date'], data['total_cases'], label='Cases')
plt.plot(data['date'], data['total_deaths'], label='Deaths')
plt.legend()

fig = px.line(data, x='date', y=['total_cases', 'total_deaths'], labels={'value':'Count', 'variable':'Metric'})

fig.show()
plt.show()