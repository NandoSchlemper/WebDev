from flask import Blueprint, render_template, url_for, flash, redirect, jsonify
from src import db
from src.models import Tickets
from src.forms import TicketForm
from dash import Dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input

Dashboard = Blueprint('Dashboard', __name__)
Dash = Dash(Dashboard)

Dash.layout = html.Div([
    html.H1("Interactive Dashboard"),
    dcc.Dropdown(
        value='SF'
    ),

    dcc.Graph(id='example-graph')
])
    
@Dash.callback(
    Output('example-graph', 'figure'),
    Input('city-dropdown', 'value')
)

def update_graph(selected_city):
        data = {
            'SF': [4, 1, 2],
            'NYC': [2, 4, 5]
        },

        return {
            'data': [
                {'x': [1,2,3], 'y': data[selected_city], 'type': 'bar', 'name': selected_city}
            ],

            'layout': {
                'title': f'bar Plots for {selected_city}'
            }
        } 
