# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dash_bootstrap_components as dbc

df = pd.read_csv('cluster_avg.csv', index_col='Unnamed: 0')
df = df.T

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Page 1", href="#")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("Page 2", href="#"),
                dbc.DropdownMenuItem("Page 3", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="Viacom Dashboard",
    brand_href="#",
    color="dark",
    dark=True,
)

row = html.Div(
    [
        dbc.Row(dbc.Col(html.Div(
                    dcc.Graph(
                        id='1',
                        figure={
                            'data': [
                                {'x': df.index, 'y': df.cluster1, 'type': 'bar', 'name': 'cluster1'},
                                {'x': df.index, 'y': df.cluster2, 'type': 'bar', 'name': 'cluster2'},
                                {'x': df.index, 'y': df.cluster3, 'type': 'bar', 'name': 'cluster3'},
                            ],
                            'layout': {
                                'title': 'Clusters'
                            }
                        }
                    )))),
        dbc.Row(
            [
                dbc.Col(html.Div(
                dcc.Graph(
                    id='2',
                    figure={
                        'data': [
                            {'x': df.index, 'y': df.cluster1, 'type': 'bar', 'name': 'cluster1'},
                            {'x': df.index, 'y': df.cluster2, 'type': 'bar', 'name': 'cluster2'},
                            {'x': df.index, 'y': df.cluster3, 'type': 'bar', 'name': 'cluster3'},
                        ],
                        'layout': {
                            'title': 'Clusters'
                        }
                    }
                ))),
                dbc.Col(html.Div(
                dcc.Graph(
                    id='3',
                    figure={
                        'data': [
                            {'x': df.index, 'y': df.cluster1, 'type': 'bar', 'name': 'cluster1'},
                            {'x': df.index, 'y': df.cluster2, 'type': 'bar', 'name': 'cluster2'},
                            {'x': df.index, 'y': df.cluster3, 'type': 'bar', 'name': 'cluster3'},
                        ],
                        'layout': {
                            'title': 'Clusters'
                        }
                    }
                ))),
            ]
        ),
    ]
)

app.layout = html.Div(children=[navbar,row])

if __name__ == '__main__':
    app.run_server()
