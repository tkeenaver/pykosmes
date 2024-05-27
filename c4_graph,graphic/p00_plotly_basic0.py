import plotly.express as px
import numpy as np

x = np.linspace(0, 10, 100)
y = np.cos(x)

fig = px.line(x=x, y=y, title='Plotly 기본 플롯', labels={'x':'x 축', 'y':'y 축'})
fig.show()

fig.update_traces(line=dict(dash='dash', color='red'))
fig.update_layout(showlegend=True, template='plotly_dark')
fig.write_image('plotly_plot.png')
