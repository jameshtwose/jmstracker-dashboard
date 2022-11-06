import dash_auth
from dash import Dash, dcc, html, Input, Output
import plotly
from dotenv import load_dotenv, find_dotenv
import dash_bootstrap_components as dbc
from database import get_user_info, add_unhash_password_column
from data_viz.tables import render_tables
load_dotenv(find_dotenv())

external_stylesheets=[dbc.themes.BOOTSTRAP, 'https://codepen.io/chriddyp/pen/bWLwgP.css']

user_df = add_unhash_password_column(get_user_info())

VALID_USERNAME_PASSWORD_PAIRS = {user_df.loc[x, "username"]: user_df.loc[x, "password"] for x in user_df.index}

app = Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

app.layout = html.Div([
    html.H1('Welcome to the JmsTracker Dashboard'),
    render_tables(),
    # dcc.Dropdown(['A', 'B'], 'A', id='dropdown'),
    # dcc.Graph(id='graph')
], className='container')

# @app.callback(
#     Output('graph', 'figure'),
#     [Input('dropdown', 'value')])
# def update_graph(dropdown_value):
#     return {
#         'layout': {
#             'title': 'Graph of {}'.format(dropdown_value),
#             'margin': {
#                 'l': 20,
#                 'b': 20,
#                 'r': 10,
#                 't': 60
#             }
#         },
#         'data': [{'x': [1, 2, 3], 'y': [4, 1, 2]}]
#     }

if __name__ == '__main__':
    # app.run_server(debug=True, threaded=True)
    app.run_server(debug=False, threaded=False)