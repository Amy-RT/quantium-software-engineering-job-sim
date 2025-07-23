# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

app = Dash()

DATA_PATH = './data/prepared_pink_morsel_data.csv'
pink_morsel_df = pd.read_csv(DATA_PATH)
pink_morsel_df = pink_morsel_df.sort_values(by="date")

fig = px.line(
    pink_morsel_df,
    x='date',         
    y='total_sales',  
    title='Daily Pink Morsel sales for the period 2018-2022:' 
)
fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Total Sales ($)",
        hovermode="x unified" # Ensures consistent hover info across lines if multiple
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
])

# --- Callback to connect radio functions to graph ---
@app.callback(
    Output('visualisation', 'figure'),
    Input('region-radio-buttons', 'value')
)
def update_graph(selected_region):
    # work with a copy of the original dataframe
    df_filtered_by_region = pink_morsel_df.copy()

    chart_title = ""

    if selected_region == 'all':
        df_for_chart = df_filtered_by_region
        chart_title = 'Pink Morsel Sales Across All Regions'
    else:
        # Filter by region
        df_for_chart = df_filtered_by_region[df_filtered_by_region['region'] == selected_region]
        chart_title = f'Pink Morsel Sales in the {selected_region.title()} Region'

    # Create the line chart
    fig = px.line(
        df_for_chart,
        x='date',
        y='total_sales',
        title=chart_title
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Total Sales ($)",
        hovermode="x unified" # Ensures consistent hover info across lines if multiple
    )

    return fig


# --- Run the app ---
if __name__ == '__main__':
    app.run(debug=True)
