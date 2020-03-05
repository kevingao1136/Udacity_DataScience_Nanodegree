import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from pandas_datareader import data as web
from datetime import datetime as dt

app = dash.Dash('Hello World')

df = pd.read_csv('demo_pivot.csv')
df['hID'] = [str(i) + 'test' for i in df['hID']]

app.layout = html.Div([
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'F.13-17', 'value': 'F.13-17'},
            {'label': 'F.18-24', 'value': 'F.18-24'},
            {'label': 'F.25-34', 'value': 'F.25-34'},
            {'label': 'F.35-44', 'value': 'F.35-44'},
            {'label': 'F.45-54', 'value': 'F.45-54'},
            {'label': 'F.55-64', 'value': 'F.55-64'},
            {'label': 'F.65+', 'value': 'F.65+'},
            {'label': 'M.13-17', 'value': 'M.13-17'},
            {'label': 'M.18-24', 'value': 'M.18-24'},
            {'label': 'M.25-34', 'value': 'M.25-34'},
            {'label': 'M.35-44', 'value': 'M.35-44'},
            {'label': 'M.45-54', 'value': 'M.45-54'},
            {'label': 'M.55-64', 'value': 'M.55-64'},
            {'label': 'M.65+', 'value': 'M.65+'},
            {'label': 'U.13-17', 'value': 'U.13-17'},
            {'label': 'U.18-24', 'value': 'U.18-24'},
            {'label': 'U.25-34', 'value': 'U.25-34'},
            {'label': 'U.35-44', 'value': 'U.35-44'},
            {'label': 'U.45-54', 'value': 'U.45-54'},
            {'label': 'U.55-64', 'value': 'U.55-64'},
            {'label': 'U.65+', 'value': 'U.65+'},
        ],
        value='F.13-17'
    ),
    dcc.Graph(id='my-graph')
], style={'width': '500'})

@app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
def update_graph(selected_dropdown_value):

    data = df[['hID',selected_dropdown_value]]
    data.sort_values(selected_dropdown_value, inplace=True)
    data = data.tail(50)

    return {
        'data': [{
            'x': data[selected_dropdown_value],
            'y': data['hID'],
            'type': 'bar',
            'orientation':'h',
            }
            ],
        'layout': {'margin': {'l': 40, 'r': 0, 't': 20, 'b': 30}}
    }

app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

if __name__ == '__main__':
    app.run_server()
