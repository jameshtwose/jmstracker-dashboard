import dash_auth
from dash import Dash, dcc, html, Input, Output
import plotly
from dotenv import load_dotenv, find_dotenv
import os
from database import get_user_info, add_unhash_password_column
load_dotenv(find_dotenv())

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

user_df = add_unhash_password_column(get_user_info())

VALID_USERNAME_PASSWORD_PAIRS = {user_df.loc[x, "username"]: user_df.loc[x, "password"] for x in user_df.index}

app = Dash(__name__, external_stylesheets=external_stylesheets)
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

app.layout = html.Div([
    html.H1('Welcome to the app'),
    html.H3('You are successfully authorized'),
    dcc.Dropdown(['A', 'B'], 'A', id='dropdown'),
    dcc.Graph(id='graph')
], className='container')

@app.callback(
    Output('graph', 'figure'),
    [Input('dropdown', 'value')])
def update_graph(dropdown_value):
    return {
        'layout': {
            'title': 'Graph of {}'.format(dropdown_value),
            'margin': {
                'l': 20,
                'b': 20,
                'r': 10,
                't': 60
            }
        },
        'data': [{'x': [1, 2, 3], 'y': [4, 1, 2]}]
    }

if __name__ == '__main__':
    app.run_server(debug=True)