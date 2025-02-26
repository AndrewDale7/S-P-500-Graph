

import matplotlib.pyplot as plt

# Read the data file
file_name = "data.dat"
years = []
closing_prices = []
annual_changes = []

with open(file_name, 'r') as file:
    for line in file:
        parts = line.strip().split('\t')  # Assuming tab-separated values
        if len(parts) < 7:  # Ensure we have enough columns
            continue  # Skip invalid lines
        
        try:
            year = int(parts[0].strip())  
            close_price = float(parts[4].strip().replace(',', ''))  
            change = float(parts[6].strip().replace('%', '').replace(',', ''))  # Use the correct column
        except ValueError:
            continue  # Skip lines with conversion errors
        
        years.append(year)
        closing_prices.append(close_price)
        annual_changes.append(change)

# Ensure data is sorted in ascending order of year
sorted_data = sorted(zip(years, closing_prices, annual_changes), key=lambda x: x[0])
years, closing_prices, annual_changes = zip(*sorted_data)

# Debugging output
for y, c, a in zip(years, closing_prices, annual_changes):
    print(f"Year: {y}, Closing Price: {c}, Annual Change: {a}%")  # Verify the correct column is used

# Plot Closing Prices
plt.figure(figsize=(12, 6))
plt.plot(years, closing_prices, marker='o', linestyle='-', color='blue', label='Year Close')
plt.xlabel('Year')
plt.ylabel('Closing Price')
plt.title('S&P 500 Yearly Closing Prices')
plt.legend()
plt.grid()
plt.show()

# Plot Annual Percentage Changes
plt.figure(figsize=(12, 6))
plt.bar(years, annual_changes, color=['red' if x < 0 else 'green' for x in annual_changes])
plt.xlabel('Year')
plt.ylabel('Annual % Change (%)')
plt.title('S&P 500 Annual Percentage Changes')
plt.axhline(0, color='black', linewidth=1)  # Baseline at 0%
plt.grid(axis='y')
plt.show()


