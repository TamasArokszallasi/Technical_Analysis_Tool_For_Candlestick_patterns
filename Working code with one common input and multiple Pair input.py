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
def analyze_data(df, pair):  # Added 'pair' as a parameter
    # Define expected movements for the top 20 patterns
    pattern_expectations = {
        'Hammer': ('bullish', 'CDLHAMMER'),
        'Shooting Star': ('bearish', 'CDLSHOOTINGSTAR'),
        'Bullish Engulfing': ('bullish', 'CDLENGULFING'),
        'Bearish Engulfing': ('bearish', 'CDLENGULFING'),
        'Evening Star': ('bearish', 'CDLEVENINGSTAR'),
        'Morning Star': ('bullish', 'CDLMORNINGSTAR'),
        'Bullish Harami': ('bullish', 'CDLHARAMI'),
        'Bearish Harami': ('bearish', 'CDLHARAMI'),
        'Three Black Crows': ('bearish', 'CDL3BLACKCROWS'),
        'Three White Soldiers': ('bullish', 'CDL3WHITESOLDIERS'),
        'Gravestone Doji': ('bearish', 'CDLGRAVESTONEDOJI'),
        'Dragonfly Doji': ('bullish', 'CDLDRAGONFLYDOJI'),
        'Bullish Long Legged Doji': ('bullish','CDLLONGLEGGEDDOJI'),
        'Bearish Long Legged Doji': ('bearish','CDLLONGLEGGEDDOJI'),
        'Marubozu': ('continuation', 'CDLMARUBOZU'),
        'Hanging Man': ('bearish', 'CDLHANGINGMAN'),
        'Inverted Hammer': ('bullish', 'CDLINVERTEDHAMMER'),
        'Piercing Line': ('bullish', 'CDLPIERCING'),
        'Dark Cloud Cover': ('bearish', 'CDLDARKCLOUDCOVER'),
    }

    # Prepare a list to store detected patterns
    detected_patterns = []

    # Detect each pattern and add corresponding rows to the detected_patterns list
    for pattern_name, (expectation, pattern_function) in pattern_expectations.items():
        pattern_detection = getattr(talib, pattern_function)(df['Open'], df['High'], df['Low'], df['Close'])
        for i in range(len(df)):
            if pattern_detection[i] != 0:
                # Apply condition for bullish patterns
                if expectation == 'bullish' and df['Close'][i] <= df['Open'][i]:
                    continue
                # Apply condition for bearish patterns
                if expectation == 'bearish' and df['Close'][i] >= df['Open'][i]:
                    continue
                # For indecision patterns, we don't check for close vs. open
                outcome = check_movement(i, expectation, df)
                detected_patterns.append([df['Date'][i], pair, pattern_name, expectation, outcome])  # Use 'pair' directly

    # Convert the list to a DataFrame
    patterns_df = pd.DataFrame(detected_patterns, columns=['Date', 'Pair', 'Pattern', 'Signal', 'Outcome'])
    
    return patterns_df

def main():
    pairs = []
    periods = []
    
    # Get common inputs once
    period = input("Enter the period (D for daily, W for weekly, M for monthlyHUF): ").lower()
    start_date = input("Enter the start date (YYYYMMDD): ")
    end_date = input("Enter the end date (YYYYMMDD): ")

    # Loop to get currency pairs
    while True:
        pair = input("Enter the currency pair (e.g., HUFEUR): ").upper()
        pairs.append(pair)
        
        more_data = input("Do you want to add another currency pair? (y/n): ").lower()
        if more_data != 'y':
            break

    # Create a personalized filename
    filename = f"Currency_Data_{'_'.join(pairs)}_{period}_{start_date}_{end_date}.xlsx"
    
    # Create an Excel writer object
    all_raw_data = []
    all_analyzed_data = []

    for pair in pairs:
        try:
            df = fetch_and_save_data(pair, period, start_date, end_date)
            if df.empty:
                print(f"No data returned for {pair}. Skipping this pair.")
                continue  # Skip to next dataset if no data is returned
            all_raw_data.append(df)  # Collect raw data
            analyzed_df = analyze_data(df, pair)  # Pass the pair variable
            if not analyzed_df.empty:
                all_analyzed_data.append(analyzed_df)  # Collect analyzed data
            else:
                print(f"No patterns detected for {pair}")
        except Exception as e:
            print(f"Failed to fetch or analyze data for {pair} with period {period} from {start_date} to {end_date}. Error: {e}")

    # Combine all data into single DataFrames, only if there's data to combine
    if all_raw_data:
        combined_raw_df = pd.concat(all_raw_data, ignore_index=True)
    else:
        print("No raw data collected.")
        combined_raw_df = pd.DataFrame()  # Empty DataFrame for raw data

    if all_analyzed_data:
        combined_analyzed_df = pd.concat(all_analyzed_data, ignore_index=True)
    else:
        print("No analyzed data collected.")
        combined_analyzed_df = pd.DataFrame()  # Empty DataFrame for analyzed data

    with ExcelWriter(filename) as writer:
        combined_raw_df.to_excel(writer, sheet_name='All_Raw_Data', index=False)  # Save all raw data in one sheet
        combined_analyzed_df.to_excel(writer, sheet_name='All_Analyzed_Data', index=False)  # Save all analyzed data in one sheet

    print(f"Data successfully saved to {filename}")

if __name__ == "__main__":
    main()
