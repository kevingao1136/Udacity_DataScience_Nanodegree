# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

df = pd.read_csv('cluster_avg.csv', index_col='Unnamed: 0')
df = df.T

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df.index, 'y': df.cluster1, 'type': 'bar', 'name': 'cluster1'},
                {'x': df.index, 'y': df.cluster2, 'type': 'bar', 'name': 'cluster2'},
                {'x': df.index, 'y': df.cluster3, 'type': 'bar', 'name': 'cluster3'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server()
