import yfinance as yf
from .patterns import *
import plotly.graph_objs as go
import pandas as pd

def getData(symbol):
    today = pd.to_datetime('today')
    one_month_ago = today - pd.DateOffset(months=1)
    df = yf.download(symbol, one_month_ago, today) 
    return df

def make_chart(df, symbol, date):
    date = pd.to_datetime(date)

    start_date = date - pd.DateOffset(days=30)
    end_date = pd.to_datetime('today')

    df_filtered = df[(df.index >= start_date) & (df.index <= end_date)]

    candlestick = go.Candlestick(x=df_filtered.index,
                                 open=df_filtered['Open'],
                                 high=df_filtered['High'],
                                 low=df_filtered['Low'],
                                 close=df_filtered['Close'])

    layout = go.Layout(title=f"Candlestick chart for {symbol}",
                       xaxis=dict(title='Date'),
                       yaxis=dict(title='Price'),
                       template='plotly_dark')

    fig = go.Figure(data=[candlestick], layout=layout)

    return fig


def catch_last_pattern(symbol):
    df = getData(symbol)
    result = None

    pattern_functions = [
        hammer, inverted_hammer, bullish_engulfing, piercing,
        morning_star, three_white_soldiers, hanging_man, shooting_star,
        bearish_engulfing, evening_star, three_black_crows, dark_cloud_cover,
        doji, spinning_top, falling_three_methods, rising_three_methods
    ]

    for pattern_function in pattern_functions:
        try:
            current_result = pattern_function(df)
            if result is None or current_result['date'] > result['date']:
                result = current_result
        except Exception as e:
            pass

    chart = make_chart(df, symbol, result['date'])

    return result, chart