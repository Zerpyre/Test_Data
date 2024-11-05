import pandas as pd
from matplotlib import pyplot as plt

filename = 'ohlcEURUSD_2005-2019.csv'

pd.set_option('display.max_columns', None)

df = pd.read_csv(filename)
print(list(df.columns))
print(df.head())
print(df.info())


# minimum date of the data
minDate = df['Date'].min()
# maximum date of the data
maxDate = df['Date'].max()
print(minDate, maxDate)

# sequence of dates from minDate to maxDate
Dates = pd.date_range(start=minDate, end=maxDate, freq='H')
# We convert it to DataFrame so we can work easily
df_date = pd.DataFrame({'Date': Dates})
# We obtain the list of dates that are not in our data
NotFoundInformationDate = df_date[~df_date['Date'].isin(df['Date'])]
# We can check its correctness by observing the length of the DataFrames
print(len(Dates), len(df), len(NotFoundInformationDate))
print(NotFoundInformationDate)

# Adding pip column
df['open2high'] = (df['EURUSD_high'] - df['EURUSD_open']) * 10000
df['open2low'] = (df['EURUSD_low'] - df['EURUSD_open']) * 10000
df['open2close'] = (df['EURUSD_close'] - df['EURUSD_open']) * 10000

print(df)

df['year'] = pd.DatetimeIndex(df['Date']).year
# df.set_index('open2high', inplace=True)
df['Date'] = pd.DatetimeIndex(df['Date'])
df_2018 = df[df['year'] == 2018]
df_2018[:1000].hist(column=['open2high', 'open2low', 'open2close'], bins=20, alpha=0.5, )
plt.show()

print('mean of open2high: ', df['open2high'].mean().round(0).astype(int))
print('standard deviation of open2high: ', df['open2high'].std().round(0).astype(int))
print('standard deviation of open2high: ', df['open2high'].std())
print('median of open2high: ', df['open2high'].median().round(0).astype(int))
item_counts = df['open2high_int'].value_counts()
print(item_counts)
print('mode of open2high: ', df['open2high_int'].mode()[0])