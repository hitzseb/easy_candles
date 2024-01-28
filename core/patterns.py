import talib

# BULLISH

def hammer(df):
    result = talib.CDLHAMMER(df['Open'], df['High'], df['Low'], df['Close'])
    result = result[result > 0].tail(1)
    date = result.index[0].date().strftime('%Y-%m-%d')
    return {'pattern':'Hammer', 'date':date, 'forecast':'bullish reversal'}

def inverted_hammer(df):
    result = talib.CDLINVERTEDHAMMER(df['Open'], df['High'], df['Low'], df['Close'])
    result = result[result > 0].tail(1)
    date = result.index[0].date().strftime('%Y-%m-%d')
    return {'pattern':'Inverted hammer', 'date':date, 'forecast':'bullish reversal'}

def bullish_engulfing(df):
    result = talib.CDLENGULFING(df['Open'], df['High'], df['Low'], df['Close'])
    result = result[result > 0].tail(1)
    date = result.index[0].date().strftime('%Y-%m-%d')
    return {'pattern':'Bullish engulfing', 'date':date, 'forecast':'bullish reversal'}

def piercing(df):
    result = talib.CDLPIERCING(df['Open'], df['High'], df['Low'], df['Close'])
    result = result[result > 0].tail(1)
    date = result.index[0].date().strftime('%Y-%m-%d')
    return {'pattern':'Piercing', 'date':date, 'forecast':'bullish reversal'}

def morning_star(df):
    result = talib.CDLMORNINGSTAR(df['Open'], df['High'], df['Low'], df['Close'])
    result = result[result > 0].tail(1)
    date = result.index[0].date().strftime('%Y-%m-%d')
    return {'pattern':'Morning star', 'date':date, 'forecast':'bullish reversal'}

def three_white_soldiers(df):
    result = talib.CDL3WHITESOLDIERS(df['Open'], df['High'], df['Low'], df['Close'])
    result = result[result > 0].tail(1)
    date = result.index[0].date().strftime('%Y-%m-%d')
    return {'pattern':'Three white soldiers', 'date':date, 'forecast':'bullish reversal'}

# BEARISH

def hanging_man(df):
    result = talib.CDLHANGINGMAN(df['Open'], df['High'], df['Low'], df['Close'])
    result = result[result < 0].tail(1)
    date = result.index[0].date().strftime('%Y-%m-%d')
    return {'pattern':'Hanging man', 'date':date, 'forecast':'bearish reversal'}

def shooting_star(df):
    result = talib.CDLSHOOTINGSTAR(df['Open'], df['High'], df['Low'], df['Close'])
    result = result[result < 0].tail(1)
    date = result.index[0].date().strftime('%Y-%m-%d')
    return {'pattern':'Shooting star', 'date':date, 'forecast':'bearish reversal'}

def bearish_engulfing(df):
    result = talib.CDLENGULFING(df['Open'], df['High'], df['Low'], df['Close'])
    result = result[result < 0].tail(1)
    date = result.index[0].date().strftime('%Y-%m-%d')
    return {'pattern':'Bearish engulfing', 'date':date, 'forecast':'bearish reversal'}

def evening_star(df):
    result = talib.CDLEVENINGSTAR(df['Open'], df['High'], df['Low'], df['Close'])
    result = result[result < 0].tail(1)
    date = result.index[0].date().strftime('%Y-%m-%d')
    return {'pattern':'Evening star', 'date':date, 'forecast':'bearish reversal'}

def three_black_crows(df):
    result = talib.CDL3BLACKCROWS(df['Open'], df['High'], df['Low'], df['Close'])
    result = result[result < 0].tail(1)
    date = result.index[0].date().strftime('%Y-%m-%d')
    return {'pattern':'Three black crows', 'date':date, 'forecast':'bearish reversal'}

def dark_cloud_cover(df):
    result = talib.CDLDARKCLOUDCOVER(df['Open'], df['High'], df['Low'], df['Close'])
    result = result[result < 0].tail(1)
    date = result.index[0].date().strftime('%Y-%m-%d')
    return {'pattern':'Three black crows', 'date':date, 'forecast':'bearish reversal'}

# UNDETERMINED

def doji(df):
    result = talib.CDLDOJI(df['Open'], df['High'], df['Low'], df['Close'])
    result = result[result != 0].tail(1)
    date = result.index[0].date().strftime('%Y-%m-%d')
    return {'pattern':'Doji', 'date':date, 'forecast':'lack of determination'}

def spinning_top(df):
    result = talib.CDLSPINNINGTOP(df['Open'], df['High'], df['Low'], df['Close'])
    result = result[result != 0].tail(1)
    date = result.index[0].date().strftime('%Y-%m-%d')
    return {'pattern':'Spinning top', 'date':date, 'forecast':'lack of determination'}

def falling_three_methods(df):
    result = talib.CDLRISEFALL3METHODS(df['Open'], df['High'], df['Low'], df['Close'])
    result = result[result < 0].tail(1)
    date = result.index[0].date().strftime('%Y-%m-%d')
    return {'pattern':'Falling three methods', 'date':date, 'forecast':'lack of determination'}

def rising_three_methods(df):
    result = talib.CDLRISEFALL3METHODS(df['Open'], df['High'], df['Low'], df['Close'])
    result = result[result > 0].tail(1)
    date = result.index[0].date().strftime('%Y-%m-%d')
    return {'pattern':'Rising three methods', 'date':date, 'forecast':'lack of determination'}