import requests
import pandas as pd
from pandas import ExcelWriter
from io import StringIO

# Define a function to fetch and save data
def fetch_and_save_data(pair, period, writer):
    url = f'https://stooq.com/q/d/l/?s={pair}&i={period}'  # Dynamic URL
    response = requests.get(url)
    data = response.text
    
    # Convert data to DataFrame
    df = pd.read_csv(StringIO(data))
    
    # Save each DataFrame to a different sheet
    df.to_excel(writer, sheet_name=pair, index=False)

def main():
    pairs = []
    periods = []
    
    # Loop to get user inputs
    while True:
        pair = input("Enter the currency pair (e.g., HUFEUR): ").upper()
        period = input("Enter the period (D for daily, W for weekly, M for monthly): ").lower()
        pairs.append(pair)
        periods.append(period)
        
        more_data = input("Do you want to add another dataset? (y/n): ").lower()
        if more_data != 'y':
            break
    
    # Create an Excel writer object
    with ExcelWriter('Currency_Data.xlsx') as writer:
        for pair, period in zip(pairs, periods):
            try:
                fetch_and_save_data(pair, period, writer)
            except Exception as e:
                print(f"Failed to fetch data for {pair} with period {period}. Error: {e}")
    
    print("Data successfully saved to Currency_Data.xlsx")

if __name__ == "__main__":
    main()
