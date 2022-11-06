from dash.dependencies import Input, Output, State
from dash import dcc, html, dash_table
from .Dietary_Reference_Intakes import (dri_based_on_df,
                                       overview_df,
                                       macronutrient_df,
                                       vitamin_df,
                                       mineral_df)

def render_tables():
    dri_based_on_dt = dash_table.DataTable(dri_based_on_df.to_dict('records'),
                                           [{'name': i, 'id': i} for i in dri_based_on_df.columns]
                                           )
    overview_dt = dash_table.DataTable(overview_df.to_dict('records'),
                                           [{'name': i, 'id': i} for i in overview_df.columns]
                                           )
    macronutrient_dt = dash_table.DataTable(macronutrient_df.to_dict('records'),
                                           [{'name': i, 'id': i} for i in macronutrient_df.columns]
                                           )
    vitamin_dt = dash_table.DataTable(vitamin_df.to_dict('records'),
                                           [{'name': i, 'id': i} for i in vitamin_df.columns]
                                           )
    mineral_dt = dash_table.DataTable(mineral_df.to_dict('records'),
                                           [{'name': i, 'id': i} for i in mineral_df.columns]
                                           )
    return html.Div([
        html.H5("Dietary Reference Intakes"),
        html.H6("Suggested intakes based on the following input data:"),
        dri_based_on_dt,
        html.H6("High level overview information:"),
        overview_dt,
        html.H6("Macronutrient information:"),
        macronutrient_dt,
        html.H6("Vitamin information:"),
        vitamin_dt,
        html.H6("Mineral information:"),
        mineral_dt
    ])
