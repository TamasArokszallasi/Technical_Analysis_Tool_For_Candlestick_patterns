import yfinance as yf
import pandas as pd
import os

# Define the ticker for EUR/HUF exchange rate
ticker = "EURHUF=X"

# Define the start and end dates
start_date = "2006-01-01"
end_date = "2023-12-31"

try:
    print("Downloading historical data...")
    # Download historical data from the start date to the end date with weekly interval
    data = yf.download(ticker, start=start_date, end=end_date, interval="1wk")

    if data.empty:
        print("No data retrieved. Please check the ticker symbol or your internet connection.")
    else:
        print("Data downloaded successfully.")
        print(data.head())  # Print the first few rows of the data to verify

        # Select the required columns: Open, High, Low, Close, Volume
        weekly_data = data[['Open', 'High', 'Low', 'Close', 'Volume']]
        print("Weekly data:")
        print(weekly_data.head())  # Print the first few rows to verify

        # Define the path for the Excel file
        excel_file = "EUR_HUF_Weekly_Data.xlsx"

        print(f"Saving data to {excel_file}...")
        # Save the data to an Excel file
        weekly_data.to_excel(excel_file, sheet_name="Weekly_Data")

        # Check if the file was created successfully
        if os.path.exists(excel_file):
            print(f"Weekly data successfully saved to {excel_file}")
        else:
            print("There was an issue saving the Excel file.")
except Exception as e:
    print(f"An error occurred: {e}")
