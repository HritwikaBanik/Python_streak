import pandas as pd

# Load the Excel file
file_path = r'C:\Users\91600\Documents\GitHub\Python_streak\xlsv to csv\Infy Jan 1 to March 03 performance.xlsx'
df = pd.read_excel(file_path)

# Convert to datetime and make both columns timezone-naive
df['Entry Time'] = pd.to_datetime(df['Entry Time'], errors='coerce').dt.tz_localize(None)
df['Exit Time'] = pd.to_datetime(df['Exit Time'], errors='coerce').dt.tz_localize(None)

print(f"Original Dataset Shape: {df.shape}")

# Step 1: Fix incorrect Exit Time (If it is 09:15:00 but on the next day, change it to 15:30:00 on the entry day)
for index, row in df.iterrows():
    exit_time = row['Exit Time']
    entry_time = row['Entry Time']
    
    # Check if exit time is at 09:15 AM but on the next day
    if exit_time.time() == pd.to_datetime("09:15:00").time() and exit_time.date() != entry_time.date():
        # Set Exit Time to 15:30:00 on the same Entry Day
        new_exit_time = f"{entry_time.date()} 15:30:00"
        df.at[index, 'Exit Time'] = pd.to_datetime(new_exit_time)

# Step 2: Remove concurrent trades (trades that start before the previous trade ends)
filtered_trades = []
last_exit_time = None

for index, row in df.iterrows():
    if last_exit_time is None or row['Entry Time'] >= last_exit_time:
        filtered_trades.append(row)
        last_exit_time = row['Exit Time']

# Convert filtered trades list back to a DataFrame
filtered_df = pd.DataFrame(filtered_trades)

# Save the cleaned data to a new CSV file
filtered_df.to_csv('modified_file.csv', index=False)

print("Concurrent and next-day trades have been removed.")
print(f"Filtered Dataset Shape: {filtered_df.shape}")
