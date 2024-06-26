import requests
import pandas as pd
from pandas import ExcelWriter
from io import StringIO
import talib

# Define a function to fetch and save data
def fetch_and_save_data(pair, period, start_date, end_date):
    url = f'https://stooq.com/q/d/l/?s={pair}&i={period}&d1={start_date}&d2={end_date}'  # Dynamic URL with date range
    response = requests.get(url)
    data = response.text
    
    # Convert data to DataFrame
    df = pd.read_csv(StringIO(data))
    
    # Ensure the columns are correctly named
    df.columns = ['Date', 'Open', 'High', 'Low', 'Close']
    df['Pair'] = pair  # Add a column to indicate the currency pair
    
    return df

# Function to determine if the expected movement happened within 5 days
def check_movement(index, expectation, df):
    for day in range(1, 6):
        if index + day >= len(df):
            break
        if expectation == 'bullish' and df['Close'][index + day] > df['Close'][index]:
            return f'True on day {day}'
        elif expectation == 'bearish' and df['Close'][index + day] < df['Close'][index]:
            return f'True on day {day}'
    return 'False'

# Analyze data with talib
def analyze_data(df):
    # Define expected movements for each pattern
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

    # Prepare a list to store detected patterns
    detected_patterns = []

    # Detect each pattern and add corresponding rows to the detected_patterns list
    for pattern_name, (expectation, pattern_function) in pattern_expectations.items():
        pattern_detection = getattr(talib, pattern_function)(df['Open'], df['High'], df['Low'], df['Close'])
        for i in range(len(df)):
            if pattern_detection[i] != 0:
                outcome = check_movement(i, expectation, df)
                detected_patterns.append([df['Date'][i], df['Pair'][i], pattern_name, expectation, outcome])

    # Convert the list to a DataFrame
    patterns_df = pd.DataFrame(detected_patterns, columns=['Date', 'Pair', 'Pattern', 'Signal', 'Outcome'])
    
    return patterns_df

def main():
    pairs = []
    periods = []
    start_dates = []
    end_dates = []
    
    # Loop to get user inputs
    while True:
        pair = input("Enter the currency pair (e.g., HUFEUR): ").upper()
        period = input("Enter the period (D for daily, W for weekly, M for monthly): ").lower()
        start_date = input("Enter the start date (YYYYMMDD): ")
        end_date = input("Enter the end date (YYYYMMDD): ")
        pairs.append(pair)
        periods.append(period)
        start_dates.append(start_date)
        end_dates.append(end_date)
        
        more_data = input("Do you want to add another dataset? (y/n): ").lower()
        if more_data != 'y':
            break
    
    # Create a personalized filename
    filename = f"Currency_Data_{'_'.join(pairs)}_{'_'.join(periods)}_{start_dates[0]}_{end_dates[0]}.xlsx"
    
    # Create an Excel writer object
    all_raw_data = []
    all_analyzed_data = []

    for pair, period, start_date, end_date in zip(pairs, periods, start_dates, end_dates):
        try:
            df = fetch_and_save_data(pair, period, start_date, end_date)
            all_raw_data.append(df)  # Collect raw data
            analyzed_df = analyze_data(df)
            all_analyzed_data.append(analyzed_df)  # Collect analyzed data
        except Exception as e:
            print(f"Failed to fetch or analyze data for {pair} with period {period} from {start_date} to {end_date}. Error: {e}")

    # Combine all data into single DataFrames
    combined_raw_df = pd.concat(all_raw_data, ignore_index=True)
    combined_analyzed_df = pd.concat(all_analyzed_data, ignore_index=True)

    with ExcelWriter(filename) as writer:
        combined_raw_df.to_excel(writer, sheet_name='All_Raw_Data', index=False)  # Save all raw data in one sheet
        combined_analyzed_df.to_excel(writer, sheet_name='All_Analyzed_Data', index=False)  # Save all analyzed data in one sheet

    print(f"Data successfully saved to {filename}")

if __name__ == "__main__":
    main()
