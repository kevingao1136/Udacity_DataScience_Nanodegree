import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np

cpm = pd.read_csv('cpm_estimates-15Apr19.csv');cpm.head()

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
    data['year'] = data.date.dt.year
    data['month'] = data.date.dt.month
    data = data[['demographic','cpm','date','year','month']]

    return data

cpm = clean_cpm()
cpm.head()


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='year-slider',
        min=cpm['year'].min(),
        max=cpm['year'].max(),
        value=cpm['year'].min(),
        marks={str(year): str(year) for year in cpm['year'].unique()},
        step=None
    )
])


@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('year-slider', 'value')])
def update_figure(selected_year):
    data = cpm[cpm.year == selected_year]
    traces = []
    for i in data.demographic.unique():
        data_by_demo = data[data['demographic'] == i]
        traces.append(dict(
            x=data_by_demo['date'],
            y=data_by_demo['cpm'],
            text=data_by_demo['demographic'],
            mode='markers',
            opacity=0.7,
            marker={
                'size': 10,
                'line': {'width': 0.5, 'color': 'white'}
            },
            name=i
        ))

    return {
        'data': traces,
        'layout': dict(
            xaxis={'type': 'date', 'title': 'Date'},
            yaxis={'title': 'CPM', 'range': [2, 8]},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            #legend={'x': 0, 'y': 1},
            hovermode='closest',
            transition = {'duration': 500},
        )
    }


if __name__ == '__main__':
    app.run_server()
