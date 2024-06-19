import requests
import pandas as pd

# Define the URL for historical data
url = 'https://stooq.com/q/d/l/?s=eurhuf&i=w'  # 'i=w' indicates weekly data

# Fetch the data
response = requests.get(url)
data = response.text

# Save the data to a CSV file
with open('EURHUF_weekly_data_stooq.csv', 'w') as file:
    file.write(data)

# Read the data into a pandas DataFrame
df = pd.read_csv('EURHUF_weekly_data_stooq.csv')

# Display the DataFrame
print(df)

# Save to Excel
df.to_excel('EURHUF_weekly_data_stooq.xlsx', index=False)

print("Data successfully saved to EURHUF_weekly_data_stooq.xlsx")
