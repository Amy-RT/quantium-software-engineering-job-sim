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
            style={
            'textAlign': 'center',
            'fontFamily': 'Arial, sans-serif',  
            'fontSize': '36px',                
            'color': '#333333',                
            'fontWeight': 'bold'               
            },
            id="header"),

    # html.Div(children='''
    #     Dash: A web application framework for your data.
    # '''),

    dcc.Graph(
        id='visualisation',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
