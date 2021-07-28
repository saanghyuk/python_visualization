
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go


df = pd.read_csv('../Data/mpg.csv')


data = [go.Scatter(x=df['horsepower'],
                   y=df['mpg'],
                   text = df['name'],
                   mode='markers',
                   marker=dict(
                       # size = 2*df['cylinders']
                        size = df['weight'] / 100,
                        color = df['cylinders'],
                        showscale=True
                   ))]

layout = go.Layout(title='Buble Chart', hovermode = 'closest')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)