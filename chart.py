import plotly.plotly as py
import plotly.graph_objs as go
from time import localtime,strftime

tableName = 'Test '+strftime("%a, %b %d %Y %H:%M", localtime())

def create_chart(sampleTimes,deviceStatus,filename = tableName):
    trace = go.Table(
    header = dict(values = ['Time','Device Status']),
    cells=dict(values=[sampleTimes, deviceStatus]))

    data = [trace]
    layout = go.Layout(title=filename)
   
    fig = go.Figure(data=data,layout=layout)
    plot_url = py.plot(fig, filename = filename, auto_open=False, world_readable = True)
    return plot_url