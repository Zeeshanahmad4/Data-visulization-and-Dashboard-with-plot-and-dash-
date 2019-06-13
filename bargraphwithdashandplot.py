import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd


app = dash.Dash()

# df = pd.read_csv("a.csv",skiprows=9,nrows=5,index_col=9)
df = pd.read_excel("/home/pythonist/Projects/Data_visual_table_and_graphs/example_of_data.xlsx", skiprows=9,nrows=5,index_col=9)
df.drop(df.columns[[13,14,15,16,17,18,19,20,21,20,22,23,24,25,26,27,28]], axis=1, inplace=True)


app.layout = html.Div([
    dcc.Graph(
        id='scatter3',
        figure={
            'data': [
                go.Bar(
                    x = df['Year'],
                    y = df['Total'],
                )
            ],
            'layout': go.Layout(

                title='Barchart'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server()