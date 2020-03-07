# -*- coding: utf-8 -*-
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
# Prepare the conversion data
conversion = pd.read_csv('data/page_conversion.csv')
conversion.hID = ['str' + str(i) for i in conversion.hID]

cpm = pd.read_csv('data/cpm.csv')
def clean_cpm(data=cpm):

    '''
    '''
    data['age_group'] = data['age_min'].astype('str') + '-' + data['age_max']
    data.loc[data['female'] == 1, 'gender'] = 'female'
    data.loc[data['male'] == 1, 'gender'] = 'male'
    data.loc[(data['female'] == 1) & (data['male'] == 1), 'gender'] = 'unisex'
    data['demographic'] = data['age_group'] + '.' + data['gender']
    data['cpm'] = data['cpm'].replace({0:np.nan})
    data['cpm'].fillna(value=data['cpm'].median(),inplace=True)
    data['date'] = pd.to_datetime(data['date'])
    data = data[['demographic','cpm','date']]

    return data
cpm = clean_cpm()
cpm.head()
demo = cpm.groupby('demographic').cpm.mean().sort_values()[:20]


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Project Link", href="https://github.com/kevingao1136/Viacom_Facebook_Project")),

    ],
    brand="Viacom Dashboard",
    brand_href="#",
    color="dark",
    dark=True,
)

row = html.Div(
    [
        dbc.Row(dbc.Col(html.Div(
        [
            html.H3(
            children='Conversion Funnels',
            style={
                'textAlign': 'center',
            }),
            dcc.Dropdown(
                id='funnel-dropdown',
                options=[
                    {'label': 'Impressions to CTA', 'value': 'Impressions to CTA'},
                    {'label': 'Impressions to Views', 'value': 'Impressions to Views'},
                    {'label': 'Views to CTA', 'value': 'Views to CTA'}
                ],
                value='Impressions to CTA'
            ),
            dcc.Graph(id='conversion-funnel')
        ]),
            width={"size": 10, "offset": 1})),

        dbc.Row(
            [
                dbc.Col(html.Div(
                dcc.Graph(
                    id='demographic',
                    figure={
                        'data': [
                            {'x': demo,
                            'y': demo.index,
                            'type': 'bar',
                            'orientation':'h'
                            }
                        ],
                        'layout': {
                            'title': 'Average CPM by Demographic'
                        }
                    }
                ))),
                dbc.Col(html.Div("One of three columns")),
            ],

        ),
    ]
)

app.layout = html.Div(children=[navbar,row])

@app.callback(Output('conversion-funnel', 'figure'), [Input('funnel-dropdown', 'value')])
def update_graph(selected_dropdown_value):

    data = conversion[['hID',selected_dropdown_value]]
    data.sort_values(selected_dropdown_value, inplace=True)
    data = data.tail(30)
    return {
        'data': [{
            'x': data[selected_dropdown_value],
            'y': data['hID'],
            'type': 'bar',
            'orientation':'h'
            }
            ],
        'layout': {'margin': {'l': 100, 'r': 0, 't': 10, 'b': 0}}
    }

if __name__ == '__main__':
    app.run_server()
