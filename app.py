# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv('./data/prepared_pink_morsel_data.csv')

fig = px.line(
    df,
    x='date',         # Column for the x-axis (e.g., time)
    y='total_sales',  # Column for the y-axis (e.g., value)
    title='Daily Pink Morsel sales for the period 2018-2022:' # Title of the chart
)

app.layout = html.Div(children=[
    html.H1(children=' Pink Morsel: Cross  Regional Sales History',
            style={
            'textAlign': 'center',
            'fontFamily': 'Arial, sans-serif',  # Example: Change font family
            'fontSize': '36px',                # Example: Change font size
            'color': '#333333',                # Example: Change font color
            'fontWeight': 'bold'               # Example: Change font weight
        }),

    # html.Div(children='''
    #     Dash: A web application framework for your data.
    # '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
