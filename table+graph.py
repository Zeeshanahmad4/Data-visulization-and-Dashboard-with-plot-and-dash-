import dash
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import dash_core_components as dcc
import dash_table as dt

# df = pd.read_excel("/home/pythonist/Projects/Data_visual_table_and_graphs/example_of_data.xlsx", skiprows=9,nrows=5,index_col=9)
# df.drop(df.columns[[13,14,15,16,17,18,19,20,21,20,22,23,24,25,26,27,28]], axis=1, inplace=True)
# frame = []

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.title = 'Data'

# Boostrap CSS.

AIRLINES_ADDRESSESC = pd.read_excel("/home/pythonist/Projects/Data_visual_table_and_graphs/example_of_data.xlsx", skiprows=1,nrows=5)
AIRLINES_ADDRESSESC.drop(AIRLINES_ADDRESSESC.columns[[14,15,16,17,18,19,20,21,20,22,23,24,25,26,27,28,29]], axis=1, inplace=True)


AIRLINES_ADDRESSESM = pd.read_excel("/home/pythonist/Projects/Data_visual_table_and_graphs/example_of_data.xlsx", skiprows=1,nrows=5)
AIRLINES_ADDRESSESM.drop(AIRLINES_ADDRESSESM.columns[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]], axis=1, inplace=True)

AIRLINES_ADDRESSESM = AIRLINES_ADDRESSESM.rename(columns = {"Jan.1": "Jan", 
                                  "Feb.1":"Feb", 
                                  "Mar.1": "Mar",
                                  "Apr.1": "Apr", 
                                  "May.1":"May", 
                                  "Jun.1": "Jun",
                                  "Jul.1": "Jul", 
                                  "Aug.1":"Aug", 
                                  "Sep.1": "Sep",
                                  "Oct.1": "OCT", 
                                  "Nov.1":"Nov", 
                                  "Dec.1": "Dec",
                                  "Total.1": "Total"}) 


#AIRPORTS
AIRPORTSC = pd.read_excel("/home/pythonist/Projects/Data_visual_table_and_graphs/example_of_data.xlsx", skiprows=9,nrows=5)
AIRPORTSC.drop(AIRPORTSC.columns[[14,15,16,17,18,19,20,21,20,22,23,24,25,26,27,28,29]], axis=1, inplace=True)


AIRPORTSM = pd.read_excel("/home/pythonist/Projects/Data_visual_table_and_graphs/example_of_data.xlsx", skiprows=9,nrows=5)
AIRPORTSM.drop(AIRPORTSM.columns[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]], axis=1, inplace=True)

AIRPORTSM = AIRPORTSM.rename(columns = {"Jan.1": "Jan", 
                                  "Feb.1":"Feb", 
                                  "Mar.1": "Mar",
                                  "Apr.1": "Apr", 
                                  "May.1":"May", 
                                  "Jun.1": "Jun",
                                  "Jul.1": "Jul", 
                                  "Aug.1":"Aug", 
                                  "Sep.1": "Sep",
                                  "Oct.1": "OCT", 
                                  "Nov.1":"Nov", 
                                  "Dec.1": "Dec",
                                  "Total.1": "Total"}) 


#MRO
#AIRPORTS
MRO = pd.read_excel("/home/pythonist/Projects/Data_visual_table_and_graphs/example_of_data.xlsx", skiprows=17,nrows=5)
MRO.drop(MRO.columns[[14,15,16,17,18,19,20,21,20,22,23,24,25,26,27,28,29]], axis=1, inplace=True)


MROM = pd.read_excel("/home/pythonist/Projects/Data_visual_table_and_graphs/example_of_data.xlsx", skiprows=17,nrows=5)
MROM.drop(MROM.columns[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]], axis=1, inplace=True)

MROM = MROM.rename(columns = {"Jan.1": "Jan", 
                                  "Feb.1":"Feb", 
                                  "Mar.1": "Mar",
                                  "Apr.1": "Apr", 
                                  "May.1":"May", 
                                  "Jun.1": "Jun",
                                  "Jul.1": "Jul", 
                                  "Aug.1":"Aug", 
                                  "Sep.1": "Sep",
                                  "Oct.1": "OCT", 
                                  "Nov.1":"Nov", 
                                  "Dec.1": "Dec",
                                  "Total.1": "Total"}) 


OEM = pd.read_excel("/home/pythonist/Projects/Data_visual_table_and_graphs/example_of_data.xlsx", skiprows=25,nrows=5)
OEM.drop(OEM.columns[[14,15,16,17,18,19,20,21,20,22,23,24,25,26,27,28,29]], axis=1, inplace=True)


OEMM = pd.read_excel("/home/pythonist/Projects/Data_visual_table_and_graphs/example_of_data.xlsx", skiprows=25,nrows=5)
OEMM.drop(OEMM.columns[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]], axis=1, inplace=True)

OEMM = OEMM.rename(columns = {"Jan.1": "Jan", 
                                  "Feb.1":"Feb", 
                                  "Mar.1": "Mar",
                                  "Apr.1": "Apr", 
                                  "May.1":"May", 
                                  "Jun.1": "Jun",
                                  "Jul.1": "Jul", 
                                  "Aug.1":"Aug", 
                                  "Sep.1": "Sep",
                                  "Oct.1": "OCT", 
                                  "Nov.1":"Nov", 
                                  "Dec.1": "Dec",
                                  "Total.1": "Total"}) 

CHARTER = pd.read_excel("/home/pythonist/Projects/Data_visual_table_and_graphs/example_of_data.xlsx", skiprows=33,nrows=5)
CHARTER.drop(CHARTER.columns[[14,15,16,17,18,19,20,21,20,22,23,24,25,26,27,28,29]], axis=1, inplace=True)


CHARTERM = pd.read_excel("/home/pythonist/Projects/Data_visual_table_and_graphs/example_of_data.xlsx", skiprows=33,nrows=5)
CHARTERM.drop(CHARTERM.columns[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]], axis=1, inplace=True)

CHARTERM = CHARTERM.rename(columns = {"Jan.1": "Jan", 
                                  "Feb.1":"Feb", 
                                  "Mar.1": "Mar",
                                  "Apr.1": "Apr", 
                                  "May.1":"May", 
                                  "Jun.1": "Jun",
                                  "Jul.1": "Jul", 
                                  "Aug.1":"Aug", 
                                  "Sep.1": "Sep",
                                  "Oct.1": "OCT", 
                                  "Nov.1":"Nov", 
                                  "Dec.1": "Dec",
                                  "Total.1": "Total"}) 

LESSORS = pd.read_excel("/home/pythonist/Projects/Data_visual_table_and_graphs/example_of_data.xlsx", skiprows=41,nrows=5)
LESSORS.drop(LESSORS.columns[[14,15,16,17,18,19,20,21,20,22,23,24,25,26,27,28,29]], axis=1, inplace=True)


LESSORSM = pd.read_excel("/home/pythonist/Projects/Data_visual_table_and_graphs/example_of_data.xlsx", skiprows=41,nrows=5)
LESSORSM.drop(LESSORSM.columns[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]], axis=1, inplace=True)

LESSORSM = LESSORSM.rename(columns = {"Jan.1": "Jan", 
                                  "Feb.1":"Feb", 
                                  "Mar.1": "Mar",
                                  "Apr.1": "Apr", 
                                  "May.1":"May", 
                                  "Jun.1": "Jun",
                                  "Jul.1": "Jul", 
                                  "Aug.1":"Aug", 
                                  "Sep.1": "Sep",
                                  "Oct.1": "OCT", 
                                  "Nov.1":"Nov", 
                                  "Dec.1": "Dec",
                                  "Total.1": "Total"}) 

OTHERS = pd.read_excel("/home/pythonist/Projects/Data_visual_table_and_graphs/example_of_data.xlsx", skiprows=49,nrows=5)
OTHERS.drop(OTHERS.columns[[14,15,16,17,18,19,20,21,20,22,23,24,25,26,27,28,29]], axis=1, inplace=True)


OTHERSM = pd.read_excel("/home/pythonist/Projects/Data_visual_table_and_graphs/example_of_data.xlsx", skiprows=49,nrows=5)
OTHERSM.drop(OTHERSM.columns[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]], axis=1, inplace=True)

OTHERSM = OTHERSM.rename(columns = {"Jan.1": "Jan", 
                                  "Feb.1":"Feb", 
                                  "Mar.1": "Mar",
                                  "Apr.1": "Apr", 
                                  "May.1":"May", 
                                  "Jun.1": "Jun",
                                  "Jul.1": "Jul", 
                                  "Aug.1":"Aug", 
                                  "Sep.1": "Sep",
                                  "Oct.1": "OCT", 
                                  "Nov.1":"Nov", 
                                  "Dec.1": "Dec",
                                  "Total.1": "Total"}) 

TOTAL = pd.read_excel("/home/pythonist/Projects/Data_visual_table_and_graphs/example_of_data.xlsx", skiprows=57,nrows=8)
TOTAL.drop(TOTAL.columns[[14,15,16,17,18,19,20,21,20,22,23,24,25,26,27,28,29]], axis=1, inplace=True)


TOTALM = pd.read_excel("/home/pythonist/Projects/Data_visual_table_and_graphs/example_of_data.xlsx", skiprows=57,nrows=8)
TOTALM.drop(TOTALM.columns[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]], axis=1, inplace=True)

TOTALM = TOTALM.rename(columns = {"Jan.1": "Jan", 
                                  "Feb.1":"Feb", 
                                  "Mar.1": "Mar",
                                  "Apr.1": "Apr", 
                                  "May.1":"May", 
                                  "Jun.1": "Jun",
                                  "Jul.1": "Jul", 
                                  "Aug.1":"Aug", 
                                  "Sep.1": "Sep",
                                  "Oct.1": "OCT", 
                                  "Nov.1":"Nov", 
                                  "Dec.1": "Dec",
                                  "Total.1": "Total"}) 

app.layout = html.Div(
    html.Div([
        html.Div([
        html.Div([ html.H4(children='AIRLINES',
                    className = "six column"),
                                        html.H4(children='MODIFIED',
                    className = "six column",
                    style={
                    'height': '14%',
                    'width': '14%',
                    'float': 'right',
                    'position': 'relative',
                    'margin-top': 20,
                    'margin-right': 20
                }),
                    html.H4(children='CREATED',
                    className = "six column",
                    style={
                    'height': '14%',
                    'width': '14%',
                    'float': 'left',
                    'position': 'relative',
                    'margin-top': 20,
                    'margin-right': 20
                }),
        ]),

                    
        
        ], className = "row",),


        html.Div([
            html.Div([
dt.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in AIRLINES_ADDRESSESC.columns],
    data=AIRLINES_ADDRESSESC.to_dict('records'),
    css= [
        
        
        {'selector': 'tr:hover',  'rule': 'background-color: pink;'
        
        }],
    style_header={'backgroundColor': 'rgb(0, 40, 80)'},


    style_cell={
        'whiteSpace': 'no-wrap',
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
        'backgroundColor': 'rgb(2, 97, 192)',
        'color': 'white',
        'text':'bold',
        'font-weight':'bold',
        'font-size': 'large'
    }
)
            ], className = 'six columns'),
        html.Div([
dt.DataTable(
    id='table2',
    columns=[{"name": i, "id": i} for i in AIRLINES_ADDRESSESM.columns],
    data=AIRLINES_ADDRESSESM.to_dict('records'),
    css= [
        
        
        {'selector': 'tr:hover',  'rule': 'background-color: pink;'
        
        }],
    style_header={'backgroundColor': 'rgb(0, 40, 80)',},


    style_cell={
        'whiteSpace': 'no-wrap',
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
        'backgroundColor': 'rgb(2, 97, 192)',
        'color': 'white',
        'text':'bold',
        'font-weight':'bold',
        'font-size': 'large'
    }
)
        ], className = "six columns"  ,)
    ], className = "row")


    ,        html.Div([
            html.Div([
    dcc.Graph(
        id='scatter4',
        figure={
            'data': [
                go.Bar(
                    x = AIRLINES_ADDRESSESC['Year'],
                    y = AIRLINES_ADDRESSESC['Total'],
                    marker=dict(
                    color='rgb(60,179,113)',),
                    
                )
            ],
            'layout': go.Layout(

                title='CREATED'
            )
        }
    )
            ], className = 'six columns'),
        html.Div([
    dcc.Graph(
        id='scatter3',
        figure={
            'data': [
                go.Bar(
                    x = AIRLINES_ADDRESSESM['Year'],
                    y = AIRLINES_ADDRESSESM['Total'],
                                    marker=dict(
                    color='rgb(60,179,113)',),)
            ],
            'layout': go.Layout(

                title='MODIFIED'
            )
        }
    )
        ], className = "six columns"  ,)
    ], className = "row")

,        html.Div([
        html.Div([ html.H4(children='AIRPORTS',
                    className = "six column"),
                                        html.H4(children='MODIFIED',
                    className = "six column",
                    style={
                    'height': '14%',
                    'width': '14%',
                    'float': 'right',
                    'position': 'relative',
                    'margin-top': 20,
                    'margin-right': 20
                }),
                    html.H4(children='CREATED',
                    className = "six column",
                    style={
                    'height': '14%',
                    'width': '14%',
                    'float': 'left',
                    'position': 'relative',
                    'margin-top': 20,
                    'margin-right': 20
                }),
        ]),

                    
        
        ], className = "row",),


        html.Div([
            html.Div([
dt.DataTable(
    id='table6',
    columns=[{"name": i, "id": i} for i in AIRPORTSC.columns],
    data=AIRPORTSC.to_dict('records'),
    css= [
        
        
        {'selector': 'tr:hover',  'rule': 'background-color: pink;'
        
        }],
    style_header={'backgroundColor': 'rgb(0, 40, 80)'},


    style_cell={
        'whiteSpace': 'no-wrap',
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
        'backgroundColor': 'rgb(2, 97, 192)',
        'color': 'white',
        'text':'bold',
        'font-weight':'bold',
        'font-size': 'large'
    }
)
            ], className = 'six columns'),
        html.Div([
dt.DataTable(
    id='table23',
    columns=[{"name": i, "id": i} for i in AIRPORTSM.columns],
    data=AIRPORTSM.to_dict('records'),
    css= [
        
        
        {'selector': 'tr:hover',  'rule': 'background-color: pink;'
        
        }],
    style_header={'backgroundColor': 'rgb(0, 40, 80)',},


    style_cell={
        'whiteSpace': 'no-wrap',
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
        'backgroundColor': 'rgb(2, 97, 192)',
        'color': 'white',
        'text':'bold',
        'font-weight':'bold',
        'font-size': 'large'
    }
)
        ], className = "six columns"  ,)
    ], className = "row")


    ,        html.Div([
            html.Div([
    dcc.Graph(
        id='scatter45',
        figure={
            'data': [
                go.Bar(
                    x = AIRPORTSC['Year'],
                    y = AIRPORTSC['Total'],
                    marker=dict(
                    color='rgb(60,179,113)',),
                    
                )
            ],
            'layout': go.Layout(

                title='CREATED'
            )
        }
    )
            ], className = 'six columns'),
        html.Div([
    dcc.Graph(
        id='scatter34',
        figure={
            'data': [
                go.Bar(
                    x = AIRPORTSM['Year'],
                    y = AIRPORTSM['Total'],
                                    marker=dict(
                    color='rgb(60,179,113)',),)
            ],
            'layout': go.Layout(

                title='MODIFIED'
            )
        }
    )
        ], className = "six columns"  ,)
    ], className = "row")

,        html.Div([
        html.Div([ html.H4(children='MRO    ',
                    className = "six column"),
                                        html.H4(children='MODIFIED',
                    className = "six column",
                    style={
                    'height': '14%',
                    'width': '14%',
                    'float': 'right',
                    'position': 'relative',
                    'margin-top': 20,
                    'margin-right': 20
                }),
                    html.H4(children='CREATED',
                    className = "six column",
                    style={
                    'height': '14%',
                    'width': '14%',
                    'float': 'left',
                    'position': 'relative',
                    'margin-top': 20,
                    'margin-right': 20
                }),
        ]),

                    
        
        ], className = "row",),


        html.Div([
            html.Div([
dt.DataTable(
    id='tab65le',
    columns=[{"name": i, "id": i} for i in MRO.columns],
    data=MRO.to_dict('records'),
    css= [
        
        
        {'selector': 'tr:hover',  'rule': 'background-color: pink;'
        
        }],
    style_header={'backgroundColor': 'rgb(0, 40, 80)'},


    style_cell={
        'whiteSpace': 'no-wrap',
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
        'backgroundColor': 'rgb(2, 97, 192)',
        'color': 'white',
        'text':'bold',
        'font-weight':'bold',
        'font-size': 'large'
    }
)
            ], className = 'six columns'),
        html.Div([
dt.DataTable(
    id='tab534le2',
    columns=[{"name": i, "id": i} for i in MROM.columns],
    data=MROM.to_dict('records'),
    css= [
        
        
        {'selector': 'tr:hover',  'rule': 'background-color: pink;'
        
        }],
    style_header={'backgroundColor': 'rgb(0, 40, 80)',},


    style_cell={
        'whiteSpace': 'no-wrap',
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
        'backgroundColor': 'rgb(2, 97, 192)',
        'color': 'white',
        'text':'bold',
        'font-weight':'bold',
        'font-size': 'large'
    }
)
        ], className = "six columns"  ,)
    ], className = "row")


    ,        html.Div([
            html.Div([
    dcc.Graph(
        id='scatter5344',
        figure={
            'data': [
                go.Bar(
                    x = MRO['Year'],
                    y = MRO['Total'],
                    marker=dict(
                    color='rgb(60,179,113)',),
                    
                )
            ],
            'layout': go.Layout(

                title='CREATED'
            )
        }
    )
            ], className = 'six columns'),
        html.Div([
    dcc.Graph(
        id='scatter3312',
        figure={
            'data': [
                go.Bar(
                    x = MROM['Year'],
                    y = MROM['Total'],
                                    marker=dict(
                    color='rgb(60,179,113)',),)
            ],
            'layout': go.Layout(

                title='MODIFIED'
            )
        }
    )
        ], className = "six columns"  ,)
    ], className = "row")
,        html.Div([
        html.Div([ html.H4(children='OEM',
                    className = "six column"),
                                        html.H4(children='MODIFIED',
                    className = "six column",
                    style={
                    'height': '14%',
                    'width': '14%',
                    'float': 'right',
                    'position': 'relative',
                    'margin-top': 20,
                    'margin-right': 20
                }),
                    html.H4(children='CREATED',
                    className = "six column",
                    style={
                    'height': '14%',
                    'width': '14%',
                    'float': 'left',
                    'position': 'relative',
                    'margin-top': 20,
                    'margin-right': 20
                }),
        ]),

                    
        
        ], className = "row",),


        html.Div([
            html.Div([
dt.DataTable(
    id='tahgble',
    columns=[{"name": i, "id": i} for i in OEM.columns],
    data=OEM.to_dict('records'),
    css= [
        
        
        {'selector': 'tr:hover',  'rule': 'background-color: pink;'
        
        }],
    style_header={'backgroundColor': 'rgb(0, 40, 80)'},


    style_cell={
        'whiteSpace': 'no-wrap',
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
        'backgroundColor': 'rgb(2, 97, 192)',
        'color': 'white',
        'text':'bold',
        'font-weight':'bold',
        'font-size': 'large'
    }
)
            ], className = 'six columns'),
        html.Div([
dt.DataTable(
    id='tablgdfe2',
    columns=[{"name": i, "id": i} for i in OEMM.columns],
    data=OEMM.to_dict('records'),
    css= [
        
        
        {'selector': 'tr:hover',  'rule': 'background-color: pink;'
        
        }],
    style_header={'backgroundColor': 'rgb(0, 40, 80)',},


    style_cell={
        'whiteSpace': 'no-wrap',
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
        'backgroundColor': 'rgb(2, 97, 192)',
        'color': 'white',
        'text':'bold',
        'font-weight':'bold',
        'font-size': 'large'
    }
)
        ], className = "six columns"  ,)
    ], className = "row")


    ,        html.Div([
            html.Div([
    dcc.Graph(
        id='sfdscatter4',
        figure={
            'data': [
                go.Bar(
                    x = OEM['Year'],
                    y = OEM['Total'],
                    marker=dict(
                    color='rgb(60,179,113)',),
                    
                )
            ],
            'layout': go.Layout(

                title='CREATED'
            )
        }
    )
            ], className = 'six columns'),
        html.Div([
    dcc.Graph(
        id='sdascatter3',
        figure={
            'data': [
                go.Bar(
                    x = OEMM['Year'],
                    y = OEMM['Total'],
                                    marker=dict(
                    color='rgb(60,179,113)',),)
            ],
            'layout': go.Layout(

                title='MODIFIED'
            )
        }
    )
        ], className = "six columns"  ,)
    ], className = "row")
,        html.Div([
        html.Div([ html.H4(children='CHARTER',
                    className = "six column"),
                                        html.H4(children='MODIFIED',
                    className = "six column",
                    style={
                    'height': '14%',
                    'width': '14%',
                    'float': 'right',
                    'position': 'relative',
                    'margin-top': 20,
                    'margin-right': 20
                }),
                    html.H4(children='CREATED',
                    className = "six column",
                    style={
                    'height': '14%',
                    'width': '14%',
                    'float': 'left',
                    'position': 'relative',
                    'margin-top': 20,
                    'margin-right': 20
                }),
        ]),

                    
        
        ], className = "row",),


        html.Div([
            html.Div([
dt.DataTable(
    id='tablzxse',
    columns=[{"name": i, "id": i} for i in CHARTER.columns],
    data=CHARTER.to_dict('records'),
    css= [
        
        
        {'selector': 'tr:hover',  'rule': 'background-color: pink;'
        
        }],
    style_header={'backgroundColor': 'rgb(0, 40, 80)'},


    style_cell={
        'whiteSpace': 'no-wrap',
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
        'backgroundColor': 'rgb(2, 97, 192)',
        'color': 'white',
        'text':'bold',
        'font-weight':'bold',
        'font-size': 'large'
    }
)
            ], className = 'six columns'),
        html.Div([
dt.DataTable(
    id='tablefdg2',
    columns=[{"name": i, "id": i} for i in CHARTERM.columns],
    data=CHARTERM.to_dict('records'),
    css= [
        
        
        {'selector': 'tr:hover',  'rule': 'background-color: pink;'
        
        }],
    style_header={'backgroundColor': 'rgb(0, 40, 80)',},


    style_cell={
        'whiteSpace': 'no-wrap',
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
        'backgroundColor': 'rgb(2, 97, 192)',
        'color': 'white',
        'text':'bold',
        'font-weight':'bold',
        'font-size': 'large'
    }
)
        ], className = "six columns"  ,)
    ], className = "row")


    ,        html.Div([
            html.Div([
    dcc.Graph(
        id='scattefsdr4',
        figure={
            'data': [
                go.Bar(
                    x = CHARTER['Year'],
                    y = CHARTER['Total'],
                    marker=dict(
                    color='rgb(60,179,113)',),
                    
                )
            ],
            'layout': go.Layout(

                title='CREATED'
            )
        }
    )
            ], className = 'six columns'),
        html.Div([
    dcc.Graph(
        id='scatqdter3',
        figure={
            'data': [
                go.Bar(
                    x = CHARTERM['Year'],
                    y = CHARTERM['Total'],
                                    marker=dict(
                    color='rgb(60,179,113)',),)
            ],
            'layout': go.Layout(

                title='MODIFIED'
            )
        }
    )
        ], className = "six columns"  ,)
    ], className = "row")
,        html.Div([
        html.Div([ html.H4(children='LESSORS',
                    className = "six column"),
                                        html.H4(children='MODIFIED',
                    className = "six column",
                    style={
                    'height': '14%',
                    'width': '14%',
                    'float': 'right',
                    'position': 'relative',
                    'margin-top': 20,
                    'margin-right': 20
                }),
                    html.H4(children='CREATED',
                    className = "six column",
                    style={
                    'height': '14%',
                    'width': '14%',
                    'float': 'left',
                    'position': 'relative',
                    'margin-top': 20,
                    'margin-right': 20
                }),
        ]),

                    
        
        ], className = "row",),


        html.Div([
            html.Div([
dt.DataTable(
    id='tablelmn',
    columns=[{"name": i, "id": i} for i in LESSORS.columns],
    data=LESSORS.to_dict('records'),
    css= [
        
        
        {'selector': 'tr:hover',  'rule': 'background-color: pink;'
        
        }],
    style_header={'backgroundColor': 'rgb(0, 40, 80)'},


    style_cell={
        'whiteSpace': 'no-wrap',
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
        'backgroundColor': 'rgb(2, 97, 192)',
        'color': 'white',
        'text':'bold',
        'font-weight':'bold',
        'font-size': 'large'
    }
)
            ], className = 'six columns'),
        html.Div([
dt.DataTable(
    id='tablebfsd2',
    columns=[{"name": i, "id": i} for i in LESSORSM.columns],
    data=LESSORSM.to_dict('records'),
    css= [
        
        
        {'selector': 'tr:hover',  'rule': 'background-color: pink;'
        
        }],
    style_header={'backgroundColor': 'rgb(0, 40, 80)',},


    style_cell={
        'whiteSpace': 'no-wrap',
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
        'backgroundColor': 'rgb(2, 97, 192)',
        'color': 'white',
        'text':'bold',
        'font-weight':'bold',
        'font-size': 'large'
    }
)
        ], className = "six columns"  ,)
    ], className = "row")


    ,        html.Div([
            html.Div([
    dcc.Graph(
        id='scattbcer4',
        figure={
            'data': [
                go.Bar(
                    x = LESSORS['Year'],
                    y = LESSORS['Total'],
                    marker=dict(
                    color='rgb(60,179,113)',),
                    
                )
            ],
            'layout': go.Layout(

                title='CREATED'
            )
        }
    )
            ], className = 'six columns'),
        html.Div([
    dcc.Graph(
        id='scfsdatter3',
        figure={
            'data': [
                go.Bar(
                    x = LESSORSM['Year'],
                    y = LESSORSM['Total'],
                                    marker=dict(
                    color='rgb(60,179,113)',),)
            ],
            'layout': go.Layout(

                title='MODIFIED'
            )
        }
    )
        ], className = "six columns"  ,)
    ], className = "row")
,        html.Div([
        html.Div([ html.H4(children='OTHERS',
                    className = "six column"),
                                        html.H4(children='MODIFIED',
                    className = "six column",
                    style={
                    'height': '14%',
                    'width': '14%',
                    'float': 'right',
                    'position': 'relative',
                    'margin-top': 20,
                    'margin-right': 20
                }),
                    html.H4(children='CREATED',
                    className = "six column",
                    style={
                    'height': '14%',
                    'width': '14%',
                    'float': 'left',
                    'position': 'relative',
                    'margin-top': 20,
                    'margin-right': 20
                }),
        ]),

                    
        
        ], className = "row",),


        html.Div([
            html.Div([
dt.DataTable(
    id='tabjghle',
    columns=[{"name": i, "id": i} for i in OTHERS.columns],
    data=OTHERS.to_dict('records'),
    css= [
        
        
        {'selector': 'tr:hover',  'rule': 'background-color: pink;'
        
        }],
    style_header={'backgroundColor': 'rgb(0, 40, 80)'},


    style_cell={
        'whiteSpace': 'no-wrap',
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
        'backgroundColor': 'rgb(2, 97, 192)',
        'color': 'white',
        'text':'bold',
        'font-weight':'bold',
        'font-size': 'large'
    }
)
            ], className = 'six columns'),
        html.Div([
dt.DataTable(
    id='tabledsf2',
    columns=[{"name": i, "id": i} for i in OTHERSM.columns],
    data=OTHERSM.to_dict('records'),
    css= [
        
        
        {'selector': 'tr:hover',  'rule': 'background-color: pink;'
        
        }],
    style_header={'backgroundColor': 'rgb(0, 40, 80)',},


    style_cell={
        'whiteSpace': 'no-wrap',
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
        'backgroundColor': 'rgb(2, 97, 192)',
        'color': 'white',
        'text':'bold',
        'font-weight':'bold',
        'font-size': 'large'
    }
)
        ], className = "six columns"  ,)
    ], className = "row")


    ,        html.Div([
            html.Div([
    dcc.Graph(
        id='scatteutyr4',
        figure={
            'data': [
                go.Bar(
                    x = OTHERS['Year'],
                    y = OTHERS['Total'],
                    marker=dict(
                    color='rgb(60,179,113)',),
                    
                )
            ],
            'layout': go.Layout(

                title='CREATED'
            )
        }
    )
            ], className = 'six columns'),
        html.Div([
    dcc.Graph(
        id='scakhjtter3',
        figure={
            'data': [
                go.Bar(
                    x = OTHERSM['Year'],
                    y = OTHERSM['Total'],
                                    marker=dict(
                    color='rgb(60,179,113)',),)
            ],
            'layout': go.Layout(

                title='MODIFIED'
            )
        }
    )
        ], className = "six columns"  ,)
    ], className = "row")
,        html.Div([
        html.Div([ html.H4(children='TOTAL',
                    className = "six column"),
                                        html.H4(children='MODIFIED',
                    className = "six column",
                    style={
                    'height': '14%',
                    'width': '14%',
                    'float': 'right',
                    'position': 'relative',
                    'margin-top': 20,
                    'margin-right': 20
                }),
                    html.H4(children='CREATED',
                    className = "six column",
                    style={
                    'height': '14%',
                    'width': '14%',
                    'float': 'left',
                    'position': 'relative',
                    'margin-top': 20,
                    'margin-right': 20
                }),
        ]),

                    
        
        ], className = "row",),


        html.Div([
            html.Div([
dt.DataTable(
    id='tablhgfe',
    columns=[{"name": i, "id": i} for i in TOTAL.columns],
    data=TOTAL.to_dict('records'),
    css= [
        
        
        {'selector': 'tr:hover',  'rule': 'background-color: pink;'
        
        }],
    style_header={'backgroundColor': 'rgb(0, 40, 80)'},


    style_cell={
        'whiteSpace': 'no-wrap',
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
        'backgroundColor': 'rgb(2, 97, 192)',
        'color': 'white',
        'text':'bold',
        'font-weight':'bold',
        'font-size': 'large'
    }
)
            ], className = 'six columns'),
        html.Div([
dt.DataTable(
    id='tagdfble2',
    columns=[{"name": i, "id": i} for i in TOTALM.columns],
    data=TOTALM.to_dict('records'),
    css= [
        
        
        {'selector': 'tr:hover',  'rule': 'background-color: pink;'
        
        }],
    style_header={'backgroundColor': 'rgb(0, 40, 80)',},

    style_table={
        
        'margin': '0px 0px 0px 90px'
    },
    style_cell={
        'whiteSpace': 'no-wrap',
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
        'backgroundColor': 'rgb(2, 97, 192)',
        'color': 'white',
        'text':'bold',
        'font-weight':'bold',
        'font-size': 'large'
    }
)
        ], className = "six columns"  ,)
    ], className = "row")


    ,        html.Div([
            html.Div([
    dcc.Graph(
        id='scattegdfr4',
        figure={
            'data': [
                go.Bar(
                    x = TOTAL['Year'],
                    y = TOTAL['Total'],
                    marker=dict(
                    color='rgb(60,179,113)',),
                    
                )
            ],
            'layout': go.Layout(

                title='CREATED'
            )
        }
    )
            ], className = 'six columns'),
        html.Div([
    dcc.Graph(
        id='scatterfs3',
        figure={
            'data': [
                go.Bar(
                    x = TOTALM['Year'],
                    y = TOTALM['Total'],
                                    marker=dict(
                    color='rgb(60,179,113)',),)
            ],
            'layout': go.Layout(

                title='MODIFIED'
            )
        }
    )
        ], className = "six columns"  ,)
    ], className = "row")

    ], className='ten columns offset-by-one')
)


if __name__ == '__main__':
    app.run_server()