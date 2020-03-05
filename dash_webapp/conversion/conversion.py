import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

app = dash.Dash('Hello World')

df = pd.read_csv('page_conversion.csv')
df['hID'] = [str(i) + 'test' for i in df['hID']]

app.layout = html.Div([
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'Impressions to CTA', 'value': 'Impressions to CTA'},
            {'label': 'Impressions to Views', 'value': 'Impressions to Views'},
            {'label': 'Views to CTA', 'value': 'Views to CTA'}
        ],
        value='Impressions to CTA'
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
            'orientation':'h'
            }
            ],
        'layout': {'margin': {'l': 40, 'r': 0, 't': 20, 'b': 30}}
    }

app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

if __name__ == '__main__':
    app.run_server()
