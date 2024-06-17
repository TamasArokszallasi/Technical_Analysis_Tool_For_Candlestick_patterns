import pandas as pd
import mplfinance as mpf

# Define the path to the Excel file
excel_file = "EUR_HUF_Weekly_Japanese_2006Q1_2023Q4.xlsx"

# Read the data from the Excel file
data = pd.read_excel(excel_file, sheet_name="Weekly_Data", index_col=0, parse_dates=True)

# Ensure the DataFrame is sorted by date
data.sort_index(inplace=True)

# Print the first few rows of the data to verify
print(data.head())

# Create a Japanese candlestick chart
mpf.plot(data, type='candle', style='charles', title='EUR/HUF Weekly Candlestick Chart',
         ylabel='Price (HUF)', volume=True, savefig='EUR_HUF_Weekly_Candlestick.png')

print("Candlestick chart saved as EUR_HUF_Weekly_Candlestick.png")
