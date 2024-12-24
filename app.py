#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dash_table
from dash import Dash, dcc, html, Input, Output
#from jupyter_dash import JupyterDash # pip install dash (version 2.0.0 or higher)


app = Dash(__name__)
server=app.server

#df=pd.read_json('all_berita_predict.json')


# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("Sentimen dan Topik Twitter", style={'text-align': 'center'}),
    
    dcc.Dropdown(id='dropdown',
                 options= [
                     {'label': 'Positif', 'value': 'lda_post_6_rf-balanced.html'},
                     {'label': 'Negatif', 'value': 'lda_neg_5_rf-balanced.html'}],
                 multi=False,
                 value='lda_post_6_rf-balanced.html',
                 style={'width':'40%'}),

    html.Br(),
    
    html.Div(id='countainer', children=[]),
    
    html.Iframe(id='ldavis', src='assets/lda_post_6_rf-balanced.html',
                     style=dict(position="absolute", left="0", top="100", width="100%", height="100%"))
        
    
])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='countainer', component_property='children'),
     Output(component_id='ldavis', component_property='src')],
    [Input(component_id='dropdown', component_property='value')])
    
def update_plot_src(input_value):
    
    if input_value=='lda_post_6_rf-balanced.html':
        label='Positif'
    else:
        label='Negatif'
    container = "Sentimen {}".format(label)
    return container, f'assets/{input_value}'

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=False)

