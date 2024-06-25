import pandas as pd
import plotly.graph_objs as go
from flask import Flask
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

# Load the data from the Excel file
file_path = 'Currency_Data.xlsx'
sheets = pd.read_excel(file_path, sheet_name=None)

app = Flask(__name__)

# Initialize Dash
dash_app = Dash(__name__, server=app, url_base_pathname='/dashboard/', external_stylesheets=[dbc.themes.BOOTSTRAP])

# Extract sheet names and data
sheet_names = list(sheets.keys())
dataframes = {name: sheets[name] for name in sheet_names if 'analyzed' in name}

# Define the layout of the Dash application
dash_app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Candlestick Pattern Visualization"),
            html.P("Select a currency pair and pattern to visualize:"),
            dcc.Dropdown(id='sheet-dropdown', options=[{'label': name, 'value': name} for name in sheet_names], value=sheet_names[0]),
            dcc.Dropdown(id='pattern-dropdown', options=[], value='Hammer'),
            dcc.Graph(id='candlestick-chart')
        ])
    ])
])

pattern_expectations = {
    'Hammer': ('bullish', 'CDLHAMMER'),
    'Inverted Hammer': ('bullish', 'CDLINVERTEDHAMMER'),
    'Hanging Man': ('bearish', 'CDLHANGINGMAN'),
    'Shooting Star': ('bearish', 'CDLSHOOTINGSTAR'),
    'Two Crows': ('bearish', 'CDL2CROWS'),
    'Three Black Crows': ('bearish', 'CDL3BLACKCROWS'),
    'Three Inside Up': ('bullish', 'CDL3INSIDE'),
    'Three Inside Down': ('bearish', 'CDL3INSIDE'),
    'Three-Line Strike Bullish': ('bullish', 'CDL3LINESTRIKE'),
    'Three-Line Strike Bearish': ('bearish', 'CDL3LINESTRIKE'),
    'Three Outside Up': ('bullish', 'CDL3OUTSIDE'),
    'Three Outside Down': ('bearish', 'CDL3OUTSIDE'),
    'Three Stars In The South': ('bullish', 'CDL3STARSINSOUTH'),
    'Three Advancing White Soldiers': ('bullish', 'CDL3WHITESOLDIERS'),
    'Abandoned Baby Bullish': ('bullish', 'CDLABANDONEDBABY'),
    'Abandoned Baby Bearish': ('bearish', 'CDLABANDONEDBABY'),
    'Advance Block': ('bearish', 'CDLADVANCEBLOCK'),
    'Belt-hold Bullish': ('bullish', 'CDLBELTHOLD'),
    'Belt-hold Bearish': ('bearish', 'CDLBELTHOLD'),
    'Breakaway Bullish': ('bullish', 'CDLBREAKAWAY'),
    'Breakaway Bearish': ('bearish', 'CDLBREAKAWAY'),
    'Closing Marubozu Bullish': ('bullish', 'CDLCLOSINGMARUBOZU'),
    'Closing Marubozu Bearish': ('bearish', 'CDLCLOSINGMARUBOZU'),
    'Concealing Baby Swallow': ('bullish', 'CDLCONCEALBABYSWALL'),
    'Counterattack Bullish': ('bullish', 'CDLCOUNTERATTACK'),
    'Counterattack Bearish': ('bearish', 'CDLCOUNTERATTACK'),
    'Dark Cloud Cover': ('bearish', 'CDLDARKCLOUDCOVER'),
    'Doji': ('indecision', 'CDLDOJI'),
    'Doji Star Bullish': ('bullish', 'CDLDOJISTAR'),
    'Doji Star Bearish': ('bearish', 'CDLDOJISTAR'),
    'Dragonfly Doji': ('bullish', 'CDLDRAGONFLYDOJI'),
    'Engulfing Pattern Bullish': ('bullish', 'CDLENGULFING'),
    'Engulfing Pattern Bearish': ('bearish', 'CDLENGULFING'),
    'Evening Doji Star': ('bearish', 'CDLEVENINGDOJISTAR'),
    'Evening Star': ('bearish', 'CDLEVENINGSTAR'),
    'Up-gap side-by-side white lines': ('bullish', 'CDLGAPSIDESIDEWHITE'),
    'Down-gap side-by-side white lines': ('bearish', 'CDLGAPSIDESIDEWHITE'),
    'Gravestone Doji': ('bearish', 'CDLGRAVESTONEDOJI'),
    'Harami Bullish': ('bullish', 'CDLHARAMI'),
    'Harami Bearish': ('bearish', 'CDLHARAMI'),
    'Harami Cross Bullish': ('bullish', 'CDLHARAMICROSS'),
    'Harami Cross Bearish': ('bearish', 'CDLHARAMICROSS'),
    'High Wave': ('indecision', 'CDLHIGHWAVE'),
    'Hikkake Pattern Bullish': ('bullish', 'CDLHIKKAKE'),
    'Hikkake Pattern Bearish': ('bearish', 'CDLHIKKAKE'),
    'Modified Hikkake Pattern Bullish': ('bullish', 'CDLHIKKAKEMOD'),
    'Modified Hikkake Pattern Bearish': ('bearish', 'CDLHIKKAKEMOD'),
    'Homing Pigeon': ('bullish', 'CDLHOMINGPIGEON'),
    'Identical Three Crows': ('bearish', 'CDLIDENTICAL3CROWS'),
    'In-Neck Pattern': ('bearish', 'CDLINNECK'),
    'Kicking Bullish': ('bullish', 'CDLKICKING'),
    'Kicking Bearish': ('bearish', 'CDLKICKING'),
    'Kicking - bull/bear determined by the longer marubozu Bullish': ('bullish', 'CDLKICKINGBYLENGTH'),
    'Kicking - bull/bear determined by the longer marubozu Bearish': ('bearish', 'CDLKICKINGBYLENGTH'),
    'Ladder Bottom': ('bullish', 'CDLLADDERBOTTOM'),
    'Long Legged Doji': ('indecision', 'CDLLONGLEGGEDDOJI'),
    'Long Line Candle': ('indecision', 'CDLLONGLINE'),
    'Marubozu Bullish': ('bullish', 'CDLMARUBOZU'),
    'Marubozu Bearish': ('bearish', 'CDLMARUBOZU'),
    'Matching Low': ('bullish', 'CDLMATCHINGLOW'),
    'Mat Hold': ('bullish', 'CDLMATHOLD'),
    'Morning Doji Star': ('bullish', 'CDLMORNINGDOJISTAR'),
    'Morning Star': ('bullish', 'CDLMORNINGSTAR'),
    'On-Neck Pattern': ('bearish', 'CDLONNECK'),
    'Piercing Pattern': ('bullish', 'CDLPIERCING'),
    'Rickshaw Man': ('indecision', 'CDLRICKSHAWMAN'),
    'Rising/Falling Three Methods Bullish': ('bullish', 'CDLRISEFALL3METHODS'),
    'Rising/Falling Three Methods Bearish': ('bearish', 'CDLRISEFALL3METHODS'),
    'Separating Lines Bullish': ('bullish', 'CDLSEPARATINGLINES'),
    'Separating Lines Bearish': ('bearish', 'CDLSEPARATINGLINES'),
    'Stalled Pattern': ('bearish', 'CDLSTALLEDPATTERN'),
    'Stick Sandwich': ('bullish', 'CDLSTICKSANDWICH'),
    'Takuri (Dragonfly Doji with very long lower shadow)': ('bullish', 'CDLTAKURI'),
    'Tasuki Gap Bullish': ('bullish', 'CDLTASUKIGAP'),
    'Tasuki Gap Bearish': ('bearish', 'CDLTASUKIGAP'),
    'Thrusting Pattern': ('bearish', 'CDLTHRUSTING'),
    'Tristar Pattern Bullish': ('bullish', 'CDLTRISTAR'),
    'Tristar Pattern Bearish': ('bearish', 'CDLTRISTAR'),
    'Unique 3 River': ('bullish', 'CDLUNIQUE3RIVER'),
    'Upside Gap Two Crows': ('bearish', 'CDLUPSIDEGAP2CROWS'),
    'Upside/Downside Gap Three Methods Bullish': ('bullish', 'CDLXSIDEGAP3METHODS'),
    'Upside/Downside Gap Three Methods Bearish': ('bearish', 'CDLXSIDEGAP3METHODS')
}

@dash_app.callback(
    [Output('pattern-dropdown', 'options'), Output('pattern-dropdown', 'value')],
    [Input('sheet-dropdown', 'value')]
)
def update_pattern_options(selected_sheet):
    if not selected_sheet:
        return [], None
    
    pattern_options = [{'label': pattern, 'value': pattern} for pattern in pattern_expectations.keys()]
    return pattern_options, pattern_options[0]['value']

@dash_app.callback(
    Output('candlestick-chart', 'figure'),
    [Input('sheet-dropdown', 'value'), Input('pattern-dropdown', 'value')]
)
def update_chart(selected_sheet, selected_pattern):
    if not selected_sheet or not selected_pattern:
        return {}

    df = dataframes[selected_sheet]
    
    # Ensure the columns are correctly named
    df.columns = ['Date', 'Open', 'High', 'Low', 'Close']

    # Create a candlestick chart
    fig = go.Figure(data=[go.Candlestick(
        x=df['Date'],
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close']
    )])

    # Highlight the selected pattern
    pattern_col = df[selected_pattern]
    for i in range(len(df)):
        if pattern_col[i] != '':
            fig.add_trace(go.Scatter(
                x=[df['Date'][i]],
                y=[df['High'][i]],
                mode='markers',
                marker=dict(color='red', size=10),
                name=selected_pattern
            ))

    fig.update_layout(
        title=f'{selected_pattern} Patterns in {selected_sheet}',
        xaxis_title='Date',
        yaxis_title='Price',
        xaxis_rangeslider_visible=False
    )

    return fig

@app.route('/')
def index():
    return 'Navigate to /dashboard/ to view the candlestick pattern visualization.'

if __name__ == '__main__':
    app.run(debug=True)
