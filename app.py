# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

DATA_PATH = './data/prepared_pink_morsel_data.csv'
df = pd.read_csv(DATA_PATH)
df = df.sort_values(by="date")

fig = px.line(
    df,
    x='date',         
    y='total_sales',  
    title='Daily Pink Morsel sales for the period 2018-2022:' 
)

app.layout = html.Div(children=[
    html.H1(children=' Pink Morsel: Cross  Regional Sales History',
            id="main-app-title",
            className='app-text-font'),
    
    dcc.Graph(
        id='visualisation',
        figure=fig
    ),

    # Add the Radio Buttons component
    html.Div(
        children=[
            html.Label('Select a Sales Region:', 
                       className='app-text-font',
                       id='radio-container-title'),
            dcc.RadioItems(
                id='region-radio-buttons', 
                className='app-text-font',
                options=[
                    {'label': 'All Regions', 'value': 'all'},
                    {'label': 'North', 'value': 'north'},
                    {'label': 'South', 'value': 'south'},
                    {'label': 'East', 'value': 'east'},
                    {'label': 'West', 'value': 'west'}
                ],
                value='all',  # Default selected value 
                inline=True,  # Display radio buttons horizontally
            )
        ],
        id='region-radio-container'
    ),

    # html.Div(children='''
    #     Dash: A web application framework for your data.
    # '''),

    

    
])

if __name__ == '__main__':
    app.run(debug=True)
