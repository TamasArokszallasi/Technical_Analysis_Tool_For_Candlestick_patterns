import pandas as pd
import pandas_ta as ta
import traceback
import os

def main():
    try:
        # Define the path to the Excel file
        excel_file = "EUR_HUF_Weekly_Data.xlsx"
        
        # Check if the file exists
        if not os.path.exists(excel_file):
            print(f"Error: The file {excel_file} does not exist.")
            return
        
        print(f"Loading data from {excel_file}...")
        
        # Load the data from the Excel file
        data = pd.read_excel(excel_file, sheet_name="Weekly_Data", index_col=0, parse_dates=True)
        print("Data loaded successfully.")

        # Print the first few rows to verify the data
        print("First few rows of the data:")
        print(data.head())

        # Clean the data: Convert prices to numeric by removing the 'Ft' string and commas
        print("Cleaning data...")
        for column in ['Open', 'High', 'Low', 'Close']:
            data[column] = data[column].astype(str).replace('[Ft,]', '', regex=True).str.replace(',', '.').astype(float)

        # Print the first few rows after cleaning to verify the data
        print("First few rows of the cleaned data:")
        print(data.head())

        # Calculate MACD
        print("Calculating MACD...")
        macd = ta.macd(data['Close'])
        print("MACD calculated successfully.")

        # Merge MACD with the original DataFrame
        print("Merging MACD with the original data...")
        data = pd.concat([data, macd], axis=1)
        print("MACD merged successfully.")

        # Determine bullish or bearish signals
        print("Determining bullish and bearish signals...")
        data['Signal'] = ''
        data['Signal'] = (data['MACD_12_26_9'] > data['MACDs_12_26_9']).astype(int).diff().fillna(0)

        # Map signal values to 'Bullish' and 'Bearish'
        data['Signal'] = data['Signal'].map({1: 'Bullish', -1: 'Bearish', 0: ''})

        # Print the first few rows with signals to verify
        print("First few rows with signals:")
        print(data[['MACD_12_26_9', 'MACDs_12_26_9', 'Signal']].head())

        # Save the result to a new Excel file
        output_file = "EUR_HUF_Weekly_Data_with_MACD_Signals.xlsx"
        print(f"Saving data with MACD and signals to {output_file}...")
        data.to_excel(output_file, sheet_name="Weekly_Data_with_MACD_Signals")
        print(f"Data with MACD and signals successfully saved to {output_file}")

    except PermissionError as pe:
        print("PermissionError:", pe)
        print("Make sure the file is not open in another program and that you have permission to read and write to it.")
    except Exception as e:
        print("An error occurred:")
        traceback.print_exc()

    # Wait for user input before closing
    input("Press Enter to close the program...")

if __name__ == "__main__":
    main()