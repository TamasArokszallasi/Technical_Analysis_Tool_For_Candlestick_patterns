import pandas as pd
import traceback
import os

def is_hammer(open_price, high_price, low_price, close_price):
    body_length = abs(close_price - open_price)
    lower_shadow = min(open_price, close_price) - low_price
    upper_shadow = high_price - max(open_price, close_price)
    
    is_hammer = (lower_shadow >= body_length) and (open_price > close_price) and (upper_shadow <= body_length) and (lower_shadow > upper_shadow * 2)
    return is_hammer

def is_inverse_hammer(open_price, high_price, low_price, close_price):
    body_length = abs(close_price - open_price)
    lower_shadow = min(open_price, close_price) - low_price
    upper_shadow = high_price - max(open_price, close_price)
    
    is_inverse_hammer = (upper_shadow >= body_length) and (close_price > open_price) and (lower_shadow <= body_length) and (upper_shadow > lower_shadow * 2)
    return is_inverse_hammer

def is_shooting_star(open_price, high_price, low_price, close_price):
    body_length = abs(close_price - open_price)
    lower_shadow = min(open_price, close_price) - low_price
    upper_shadow = high_price - max(open_price, close_price)
    
    is_shooting_star = (upper_shadow >= body_length) and (close_price > open_price) and (lower_shadow <= body_length) and (upper_shadow > lower_shadow * 2)
    return is_shooting_star

def is_hanging_man(open_price, high_price, low_price, close_price):
    body_length = abs(close_price - open_price)
    lower_shadow = min(open_price, close_price) - low_price
    upper_shadow = high_price - max(open_price, close_price)
    
    is_hanging_man = (lower_shadow >= body_length) and (open_price > close_price) and (upper_shadow <= body_length) and (lower_shadow > upper_shadow * 2)
    return is_hanging_man

def check_signal_validity(data, index, periods=3, pattern='hammer'):
    if index + periods >= len(data):
        return 'Undetermined'
    
    initial_close = data.iloc[index]['Close']
    
    if pattern in ['hammer', 'hanging_man']:
        for i in range(1, periods + 1):
            if data.iloc[index + i]['Close'] <= initial_close:
                return 'False'
    elif pattern in ['inverse_hammer', 'shooting_star']:
        for i in range(1, periods + 1):
            if data.iloc[index + i]['Close'] >= initial_close:
                return 'False'
    return 'True'

def is_downtrend(data, index):
    if index < 3:
        return False
    for i in range(1, 4):
        if data.iloc[index - i]['Open'] <= data.iloc[index - i]['Close']:
            return False
    return True

def is_uptrend(data, index):
    if index < 3:
        return False
    for i in range(1, 4):
        if data.iloc[index - i]['Open'] >= data.iloc[index - i]['Close']:
            return False
    return True

def main():
    try:
        excel_file = "EURHUF_Weekly_Data.xlsx"
        
        if not os.path.exists(excel_file):
            print(f"Error: The file {excel_file} does not exist.")
            return
        
        print(f"Loading data from {excel_file}...")
        data = pd.read_excel(excel_file, sheet_name="Weekly_Data", index_col=0, parse_dates=True)
        print("Data loaded successfully.")
        print("First few rows of the data:")
        print(data.head())

        print("Cleaning data...")
        for column in ['Open', 'High', 'Low', 'Close']:
            data[column] = data[column].astype(str).replace('Ft', '', regex=False).str.replace(',', '.').astype(float)
        
        print("First few rows of the cleaned data:")
        print(data.head())

        print("Identifying candlestick patterns...")
        data['Hammer_Signal'] = data.apply(
            lambda row: 'Hammer' if is_hammer(row['Open'], row['High'], row['Low'], row['Close']) else '', axis=1)
        data['Inverse_Hammer_Signal'] = data.apply(
            lambda row: 'Inverse Hammer' if is_inverse_hammer(row['Open'], row['High'], row['Low'], row['Close']) else '', axis=1)
        data['Shooting_Star_Signal'] = data.apply(
            lambda row: 'Shooting Star' if is_shooting_star(row['Open'], row['High'], row['Low'], row['Close']) else '', axis=1)
        data['Hanging_Man_Signal'] = data.apply(
            lambda row: 'Hanging Man' if is_hanging_man(row['Open'], row['High'], row['Low'], row['Close']) else '', axis=1)
        
        print("Applying trend conditions...")
        for i in range(len(data)):
            if data.iloc[i]['Hammer_Signal'] == 'Hammer':
                if not is_downtrend(data, i):
                    data.at[data.index[i], 'Hammer_Signal'] = ''
            if data.iloc[i]['Inverse_Hammer_Signal'] == 'Inverse Hammer':
                if not is_downtrend(data, i):
                    data.at[data.index[i], 'Inverse_Hammer_Signal'] = ''
            if data.iloc[i]['Shooting_Star_Signal'] == 'Shooting Star':
                if not is_uptrend(data, i):
                    data.at[data.index[i], 'Shooting_Star_Signal'] = ''
            if data.iloc[i]['Hanging_Man_Signal'] == 'Hanging Man':
                if not is_uptrend(data, i):
                    data.at[data.index[i], 'Hanging_Man_Signal'] = ''

        print("Verifying candlestick pattern signals...")
        data['Hammer_Validity'] = ''
        data['Inverse_Hammer_Validity'] = ''
        data['Shooting_Star_Validity'] = ''
        data['Hanging_Man_Validity'] = ''
        
        for i in range(len(data)):
            if data.iloc[i]['Hammer_Signal'] == 'Hammer':
                data.at[data.index[i], 'Hammer_Validity'] = check_signal_validity(data, i, pattern='hammer')
            if data.iloc[i]['Inverse_Hammer_Signal'] == 'Inverse Hammer':
                data.at[data.index[i], 'Inverse_Hammer_Validity'] = check_signal_validity(data, i, pattern='inverse_hammer')
            if data.iloc[i]['Shooting_Star_Signal'] == 'Shooting Star':
                data.at[data.index[i], 'Shooting_Star_Validity'] = check_signal_validity(data, i, pattern='shooting_star')
            if data.iloc[i]['Hanging_Man_Signal'] == 'Hanging Man':
                data.at[data.index[i], 'Hanging_Man_Validity'] = check_signal_validity(data, i, pattern='hanging_man')
        
        print("Printing identified patterns...")
        patterns = data[(data['Hammer_Signal'] == 'Hammer') | 
                        (data['Inverse_Hammer_Signal'] == 'Inverse Hammer') | 
                        (data['Shooting_Star_Signal'] == 'Shooting Star') | 
                        (data['Hanging_Man_Signal'] == 'Hanging Man')]
        
        print(patterns[['Open', 'High', 'Low', 'Close', 'Hammer_Signal', 'Hammer_Validity',
                        'Inverse_Hammer_Signal', 'Inverse_Hammer_Validity',
                        'Shooting_Star_Signal', 'Shooting_Star_Validity',
                        'Hanging_Man_Signal', 'Hanging_Man_Validity']])
        
        output_file = "EUR_HUF_Weekly_Data_with_Candlestick_Patterns.xlsx"
        print(f"Saving data with candlestick patterns to {output_file}...")
        data.to_excel(output_file, sheet_name="Weekly_Data_with_Candlestick_Patterns")
        print(f"Data with candlestick patterns successfully saved to {output_file}")

    except PermissionError as pe:
        print("PermissionError:", pe)
        print("Make sure the file is not open in another program and that you have permission to read and write to it.")
    except Exception as e:
        print("An error occurred:")
        traceback.print_exc()

    input("Press Enter to close the program...")

if __name__ == "__main__":
    main()
