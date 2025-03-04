from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import numpy as np
import plotly.express as px
import pandas as pd
import plotly.graph_objs as go
from scipy.stats import linregress
import urllib.request
import certifi
import ssl
import json
url = (
    "https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/5950/JSON?heading=Solubility.")

context = ssl.create_default_context(cafile=certifi.where())
result = urllib.request.urlopen(url, context=context)


#jsonurl = urllib.request.urlopen(url)
#data_sol = str(json.loads(result.read()))
data_sol = 'Maoz Lahav'


#data_sol = json.load(url)


#df = pd.read_csv('https://raw.githubusercontent.com/dandindan/CS50p/main/all%20metabolites%2021.12.22.csv')
#df = pd.read_csv('/home/dandin/mysite/data/21-12-22.csv')
#df = pd.read_parquet('/home/dandin/mysite/data/all_matabolites_21_12_22.parquet.gzip')

# delete the line below and un pound the first csv
df = pd.read_csv(
    '/Users/maozlahav/Documents/GitHub/CS50p/all metabolites 21.12.22.csv')


def set_dtypes(df):
    df['Time'] = df['Time'].astype('float32')
    # ###df['Strain'] = df['Strain'].astype('category')
    df['Strain'] = df['Strain'].astype('str')
    df['Metabolite'] = df['Metabolite'].astype('category')
    df['Concentration'] = df['Concentration'].astype('float32')
    df['Date'] = df['Date'].astype('category')
    # ####df["Date"] = pd.to_datetime(df["Date"], format='%d%m%y')
    df['Number'] = df['Number'].astype('int32')
    # ###df['Number'] = df['Number'].astype('category')
    df['OD600'] = df['OD600'].astype('float32')
    return df


df = set_dtypes(df)  # set datatypes

list_metabolites = df.Metabolite.unique()
metabo2 = 'Alanine'
app = Dash(__name__, )
server = app.server
app.title = 'Metabolite'
upper_layout = html.Div([



    html.Div([
        html.Div([
            html.P('Select Metabolite:', className='fix_label',
                   style={'color': 'white'}),
            dcc.Dropdown(id='metabo2',
                         multi=False,
                         clearable=False,
                         disabled=False,
                         style={'display': True},
                         value='Alanine',
                         placeholder='Select Matabolite',
                         options=[{'label': c, 'value': c}
                                  for c in list_metabolites], className='dcc_compon'),

            html.P('Select Repetition:', className='fix_label',
                   style={'color': 'white'}),
            dcc.RadioItems(id='reps2',
                           inline=True,
                           labelStyle={
                               'padding-left': 20, },

                           options=[],
                           className='dcc_compon'),


            html.P('Select Concentration:', className='fix_label', style={
                   'color': 'white', 'margin-left': '1%'}),

            dcc.RangeSlider(id='select_conc2',
                            min=0,
                            max=500,
                            tooltip={"placement": "topLeft",
                                     "always_visible": True},
                            value=[0, 500],
                            updatemode='drag'),

            html.P('The Concentration:', className='fix_label', style={
                   'color': 'white', 'margin-left': '1%'}),

             html.P(id='list_rep_conc2', className='fix_label', style={
                 'color': 'white',  'fontSize': 14, 'margin-left': '1%'}),

             html.P('Select Time:', className='fix_label', style={
                 'color': 'white', 'margin-left': '1%'}),

             dcc.RangeSlider(id='select_time_up',
                             min=0,
                             max=60,
                             step=5,
                             tooltip={"placement": "topLeft",
                                      "always_visible": True},
                             value=[0, 60],
                             updatemode='drag'),

             html.P('Select:  ', className='fix_label', style={
                 'color': 'white', 'margin-left': '1%'}),
             html.Div([
                 html.Div(['Regression', dcc.Input(id='range1', type='number', min=2, max=12,
                                                   step=1, value=5)]),
                 html.Div(['Length', dcc.Input(
                     id='range2', type='number', min=0, max=20, step=1, value=4, )]),
                 html.Div(['Percent', dcc.Input(
                     id='range3', type='number', min=5, max=100, step=5, value=25, )]),
                 html.Div(['Mean', dcc.Input(id='range4', type='number', min=0.1, max=5,
                                             step=0.1, value=2, )]),
             ], className='input_range'),
             #  html.Pre('  A      B      C     D', className='pre_label', style={
             #      'color': 'white', 'margin-left': '1%'}),

             ], className="create_container three columns"),

        ####################################################################################################


        html.Div([
            dcc.Loading(children=[
                dcc.Graph(id='scatter_chart_up1',
                          config={'displayModeBar': 'hover'},
                          style={"height": "100%", "width": "100%", }),
            ], color="#119DFF", type="cube", fullscreen=False),
            html.Div(data_sol, style={'color': 'white'})


        ], className="create_container six columns"),

        html.Div([
            # dcc.Graph(id='pie_chart',
            #           config={'displayModeBar': 'hover'}),
            html.Iframe(
                id='frame', src="https://pubchem.ncbi.nlm.nih.gov/compound/"+metabo2+"#section=3D-Conformer&embed=true",
                style={"height": "100%", "width": "100%", }),
        ], className="create_container three columns"),

    ], className="row flex-display"),
    ##############################################################################################
    #                                   end of first row
    ##############################################################################################
    html.Div([
        html.Div([
            dcc.Graph(id='chart_up2',
                      config={'displayModeBar': 'hover'},
                      clickData={'points': [{'x': 0}, {'x': 0}]}),


        ], className="create_container six columns"),

        html.Div([
            dcc.Graph(id='chart_up3',
                      config={'displayModeBar': 'hover'},
                      clickData={'points': [{'x': 0}, {'x': 0}]}),

        ], className="create_container six columns"),

    ], className="row flex-display"),

    ##############################################################################################
    #                                   end of second row
    ##############################################################################################

    html.Div([
        html.Div([
            dcc.Graph(id='chart_up4',
                      config={'displayModeBar': 'hover'}),

        ], className="create_container six columns"),

        html.Div([
            dcc.Graph(id='chart_up5',
                      config={'displayModeBar': 'hover'}),

        ], className="create_container six columns"),

    ], className="row flex-display"),

    ##############################################################################################
    #                                   end of third row
    ##############################################################################################


], id="mainContainer", style={"display": "flex", "flex-direction": "column"})
