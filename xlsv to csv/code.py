import pandas as pd

file_path = r'C:\Users\91600\Documents\GitHub\Python_streak\xlsv to csv\Infy Jan 1 to March 03 performance.xlsx'

df = pd.read_excel(file_path)
df.to_csv('Jan1_to_March03_Performance.csv', index=False)

o = pd.read_csv('Jan1_to_March03_Performance.csv')

# Convert 'start_time' and 'end_time' columns to datetime
o['Entry Time'] = pd.to_datetime(o['Entry Time'])
o['Exit Time'] = pd.to_datetime(o['Exit Time'])


# This will be True for the rows where the exit time is the next day
o['is_next_day'] = (o['Exit Time'].dt.date > o['Entry Time'].dt.date) &  \
                   (o['Exit Time'].dt.date - o['Entry Time'].dt.date == pd.Timedelta(days=1))

# Removed the rows where 'is_next_day' is True
o = o[~o['is_next_day']]

# Dropped the 'is_next_day' column as it's no longer needed
o = o.drop(columns=['is_next_day'])

# Save the modified DataFrame back to CSV
o.to_csv('modified_file.csv', index=False)

print("Records with 'Exit Time' being the next day of 'Entry Time' have been deleted.")


print(df)
print(o)
print(df.shape)  #(rows, columns)
print(o.shape)