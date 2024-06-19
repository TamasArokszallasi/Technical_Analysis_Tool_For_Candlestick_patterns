import pandas as pd
import traceback
import os

def is_hammer(open_price, high_price, low_price, close_price):
    body_length = abs(close_price - open_price)
    lower_shadow = min(open_price, close_price) - low_price
    upper_shadow = high_price - max(open_price, close_price)
    
    # Define the Hammer based on the new rules
    is_hammer = (lower_shadow >= body_length) and (open_price > close_price) and (upper_shadow <= body_length)
    return is_hammer

def check_hammer_signal(data, index, periods=3):
    if index + periods >= len(data):
        return 'Undetermined'
    
    initial_close = data.iloc[index]['Close']
    for i in range(1, periods + 1):
        if data.iloc[index + i]['Close'] <= initial_close:
            return 'False'
    return 'True'

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

        print("Identifying Hammer candlestick patterns...")
        data['Hammer_Signal'] = data.apply(
            lambda row: 'Hammer' if is_hammer(row['Open'], row['High'], row['Low'], row['Close']) else '', axis=1)
        
        print("Verifying Hammer signals...")
        data['Hammer_Validity'] = ''
        for i in range(len(data)):
            if data.iloc[i]['Hammer_Signal'] == 'Hammer':
                data.at[data.index[i], 'Hammer_Validity'] = check_hammer_signal(data, i)
        
        hammer_rows = data[data['Hammer_Signal'] == 'Hammer']
        print(f"Number of Hammer patterns identified: {len(hammer_rows)}")
        print(hammer_rows[['Open', 'High', 'Low', 'Close', 'Hammer_Signal', 'Hammer_Validity']])

        output_file = "EUR_HUF_Weekly_Data_with_Hammer_Signals_and_Validity.xlsx"
        print(f"Saving data with Hammer signals and validity to {output_file}...")
        data.to_excel(output_file, sheet_name="Weekly_Data_with_Hammer_Signals_and_Validity")
        print(f"Data with Hammer signals and validity successfully saved to {output_file}")

    except PermissionError as pe:
        print("PermissionError:", pe)
        print("Make sure the file is not open in another program and that you have permission to read and write to it.")
    except Exception as e:
        print("An error occurred:")
        traceback.print_exc()

    input("Press Enter to close the program...")

if __name__ == "__main__":
    main()
