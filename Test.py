#Must read the ReadMe file before starting to analyse this code.
import yfinance as yf
import pandas as pd
import pandas_ta as ta
import talib
import mplfinance as mpf

# Define the FX pairs
fx_pairs = ['HUFUSD=X', 'CZKUSD=X', 'PLNUSD=X', 'DKKUSD=X', 'SEKUSD=X', 'CHFUSD=X', 'EURUSD=X']

# Fetch weekly data from Yahoo Finance
start_date = '2006-01-01'
end_date = '2023-06-30'
data = {}

for pair in fx_pairs:
    data[pair] = yf.download(pair, start=start_date, end=end_date, interval='1wk')

# Example of HUF/EUR data
huf_eur = yf.download('HUFEUR=X', start=start_date, end=end_date, interval='1wk')

# Calculate indicators for HUF/EUR
huf_eur['SMA'] = ta.sma(huf_eur['Close'], length=14)
huf_eur['EMA'] = ta.ema(huf_eur['Close'], length=14)
huf_eur['MACD'], huf_eur['MACDSignal'], huf_eur['MACDHist'] = ta.macd(huf_eur['Close'])
huf_eur['RSI'] = ta.rsi(huf_eur['Close'], length=14)
huf_eur['UpperBB'], huf_eur['MiddleBB'], huf_eur['LowerBB'] = ta.bbands(huf_eur['Close'], length=20, std=2)
huf_eur['ATR'] = ta.atr(huf_eur['High'], huf_eur['Low'], huf_eur['Close'], length=14)
huf_eur['OBV'] = ta.obv(huf_eur['Close'], huf_eur['Volume'])

# Recognize candlestick patterns for HUF/EUR
huf_eur['Doji'] = talib.CDLDOJI(huf_eur['Open'], huf_eur['High'], huf_eur['Low'], huf_eur['Close'])
huf_eur['Hammer'] = talib.CDLHAMMER(huf_eur['Open'], huf_eur['High'], huf_eur['Low'], huf_eur['Close'])
huf_eur['HangingMan'] = talib.CDLHANGINGMAN(huf_eur['Open'], huf_eur['High'], huf_eur['Low'], huf_eur['Close'])
huf_eur['BullishEngulfing'] = talib.CDLENGULFING(huf_eur['Open'], huf_eur['High'], huf_eur['Low'], huf_eur['Close']) == 100
huf_eur['BearishEngulfing'] = talib.CDLENGULFING(huf_eur['Open'], huf_eur['High'], huf_eur['Low'], huf_eur['Close']) == -100
huf_eur['MorningStar'] = talib.CDLMORNINGSTAR(huf_eur['Open'], huf_eur['High'], huf_eur['Low'], huf_eur['Close'])
huf_eur['EveningStar'] = talib.CDLEVENINGSTAR(huf_eur['Open'], huf_eur['High'], huf_eur['Low'], huf_eur['Close'])

# Function to log pattern occurrences
def log_occurrences(df, pattern_name, signal_column):
    occurrences = df[df[signal_column] != 0][['Close', signal_column]]
    occurrences['Pattern'] = pattern_name
    occurrences['Signal'] = occurrences[signal_column].apply(lambda x: 'Bullish' if x > 0 else 'Bearish')
    occurrences['Date'] = occurrences.index
    return occurrences[['Date', 'Pattern', 'Signal', 'Close']]

# Log occurrences of patterns and indicators
patterns = ['Doji', 'Hammer', 'HangingMan', 'BullishEngulfing', 'BearishEngulfing', 'MorningStar', 'EveningStar']
occurrences_df = pd.DataFrame()

for pattern in patterns:
    occurrences_df = pd.concat([occurrences_df, log_occurrences(huf_eur, pattern, pattern)], ignore_index=True)

# Display the occurrences
print(occurrences_df)

# Plot the HUF/EUR chart with highlighted patterns
def plot_with_patterns(df, patterns_df):
    ap = []
    for _, row in patterns_df.iterrows():
        color = 'g' if row['Signal'] == 'Bullish' else 'r'
        ap.append(mpf.make_addplot(df.loc[row['Date'], 'Close'], type='scatter', markersize=100, marker='^', color=color))
    
    mpf.plot(df, type='candle', style='charles', addplot=ap, title='HUF/EUR with Patterns', volume=True)

# Plotting the chart
plot_with_patterns(huf_eur, occurrences_df)
