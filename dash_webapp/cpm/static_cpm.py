import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('cpm_estimates-15Apr19.csv')

def clean_cpm(data=df):

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

df = clean_cpm()

df

app.layout = html.Div([
    dcc.Graph(
        id='CPM',
        figure={
            'data': [
                dict(
                    x=df['date'],
                    y=df['cpm'],
                    #text=df[df['demographic'] == i]['demographic'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 10,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.demographic.unique()
            ],
            'layout': dict(
                xaxis={'type': 'log'},
                yaxis={'title': 'CPM'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
