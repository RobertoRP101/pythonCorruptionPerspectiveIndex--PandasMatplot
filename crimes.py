import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


io = r'.\Data\CPI 2015_data.xlsx'
sheet_name = 'CPI 2015'
df = pd.read_excel(io, sheet_name, header=1, names=None, index_col=None, usecols=None, dtype=None, 
                   converters=None, skiprows=0, nrows=None, na_values=['NA', '--', ''],
                   keep_default_na=True, na_filter=True, verbose=True, parse_dates=True, 
                #  date_parser=lambda x: pd.to_datetime(x, format ='%Y-%m-%d'),
                   date_format='%Y-%m-%d',
                   thousands=',', decimal='.', comment='#',
                   skipfooter=1, 
                   storage_options=None)

print(f'Columns: \n{[f'{column_name}' for column_name in  df.columns]}')
print(f'Regions: \n{set([f'{region}' for region in  df['Region']])}')


print(f'Highest 5 world bank CPIA in 2015: \n{df.sort_values(by='World Bank CPIA', ascending=False).head(5).reset_index()}')
print(f'Highest 10 Corruption Perception Index in AME region: \n{df[df["Region"] == 'AME'].sort_values(by='CPI2015', ascending=False).head(10)}')

# Ensure that only exist non-empty values
df.dropna(axis=0, how='any', subset=['Economist Intelligence Unit', 'CPI2015'], inplace=True)
x = df['Economist Intelligence Unit']
y = df['CPI2015']

# Validation of not empty values
if x.empty or y.empty:
    raise ValueError("One or both of the vectors x or y are empty.")

plt.figure(figsize=(10,6))
plt.scatter(df['Economist Intelligence Unit'], df['CPI2015'])
df = df.reset_index()
print(df.head(3))
for position, country in enumerate(df['Country']):
    plt.text(df['Economist Intelligence Unit'][position], df['CPI2015'][position], country, fontsize=9)

plt.xlabel('Economist Intelligence Unit')
plt.ylabel('CPI2015')
plt.title('Economist Intelligence Unit vs CPI2015')




# Calculate linear regression line (trend line)



if not x.isnull().values.any() and not y.isnull().values.any():
    slope, intercept = np.polyfit(x, y, 1)
    trend_line = slope * x + intercept
    print("Slope:", slope, "Intercept:", intercept)

# Get the slope and intercept for the line of best fit
slope, intercept = np.polyfit(x, y, 1)

# Create the trend line
trend_line = slope * x + intercept
plt.plot(x, trend_line, color='red', label='Trend Line')

# Show plot with grid and legend
plt.grid(True)
plt.legend()
plt.show()