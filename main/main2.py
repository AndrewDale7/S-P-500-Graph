import matplotlib.pyplot as plt
import csv
from datetime import datetime

# Read the data file
file_name = "weeklydata.csv"
dates = []
closing_prices = []
weekly_changes = []

with open(file_name, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    
    for row in reader:
        try:
            date = datetime.strptime(row[0], "%m/%d/%Y")  # Convert date string to datetime
            close_price = float(row[1].replace(',', ''))  # Convert price to float
            change = float(row[6].replace('%', '').replace(',', ''))  # Convert change to float
        except (ValueError, IndexError):
            continue  # Skip lines with errors
        
        dates.append(date)
        closing_prices.append(close_price)
        weekly_changes.append(change)

# Sort data by date in ascending order
dates, closing_prices, weekly_changes = zip(*sorted(zip(dates, closing_prices, weekly_changes)))

# Plot Weekly Closing Prices
plt.figure(figsize=(12, 6))
plt.plot(dates, closing_prices, marker='o', linestyle='-', color='blue', label='Weekly Close')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('S&P 500 Weekly Closing Prices')
plt.legend()
plt.xticks(rotation=45)
plt.grid()
plt.xlim(dates[0], dates[-1])  # Ensure x-axis is flush with data
plt.show()

# Plot Weekly Percentage Changes with improved visibility
plt.figure(figsize=(12, 6))
plt.bar(dates, weekly_changes, color=['red' if x < 0 else 'green' for x in weekly_changes], width=7)
plt.xlabel('Date')
plt.ylabel('Weekly % Change (%)')
plt.title('S&P 500 Weekly Percentage Changes')
plt.axhline(0, color='black', linewidth=1)  # Baseline at 0%
plt.ylim(-8, 8)  # Set y-axis limits to ±8%
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.xlim(dates[0], dates[-1])  # Ensure x-axis is flush with data
plt.show()
