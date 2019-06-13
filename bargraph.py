import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
# df = pd.read_csv("a.csv",skiprows=9,nrows=5,index_col=9)
df = pd.read_excel("/home/pythonist/Projects/Data_visual_table_and_graphs/example_of_data.xlsx", skiprows=9,nrows=5,index_col=9)
df.drop(df.columns[[13,14,15,16,17,18,19,20,21,20,22,23,24,25,26,27,28]], axis=1, inplace=True)


data = [go.Bar(
    x=df['Year'],  # NOC stands for National Olympic Committee
    y=df['Total']
)]
layout = go.Layout(
    title='Barchart'

)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bar1.html')