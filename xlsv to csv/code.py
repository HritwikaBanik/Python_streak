import pandas as pd

# Load the Excel file
file_path = r'C:\Users\91600\Documents\GitHub\Python_streak\xlsv to csv\Infy Jan 1 to March 03 performance.xlsx'
df = pd.read_excel(file_path)

# Convert 'Entry Time' and 'Exit Time' to datetime
df['Entry Time'] = pd.to_datetime(df['Entry Time'])
df['Exit Time'] = pd.to_datetime(df['Exit Time'])

# Ensure data is sorted by Entry Time
#df = df.sort_values(by='Entry Time')

print(f"Original Dataset: {df.shape}")

# Remove trades where Exit Time is on the next day
df = df[df['Exit Time'].dt.date == df['Entry Time'].dt.date]

# List to store filtered trades
filtered_trades = []
last_exit_time = None

# Iterate over trades to remove concurrent trades
for index, row in df.iterrows():
    if last_exit_time is None or row['Entry Time'] >= last_exit_time:
        filtered_trades.append(row)
        last_exit_time = row['Exit Time']

# Convert back to DataFrame
filtered_df = pd.DataFrame(filtered_trades)

# Save the modified DataFrame back to CSV
filtered_df.to_csv('modified_file.csv', index=False)

print("Concurrent and next-day trades have been removed.")
print(f"Original trades on the same day: {df.shape}, Filtered trades(without concurrency): {filtered_df.shape}")
