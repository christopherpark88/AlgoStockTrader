import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

# start = dt.datetime(2000,1,1)
# end = dt.datetime(2020,10,31)
#
# dataFrame = web.DataReader('TSLA', 'yahoo', start, end)
# dataFrame.to_csv('tsla.csv')

dataFrame = pd.read_csv('tsla.csv', parse_dates = True, index_col = 0)
#dataFrame['100ma'] = dataFrame['Adj Close'].rolling(window=100, min_periods = 0).mean()

#OHLC is Open High Low Close
dataFrame_ohlc = dataFrame['Adj Close'].resample('10D').ohlc()
dataFrame_volume = dataFrame['Volume'].resample('10D').sum()

dataFrame_ohlc.reset_index(inplace=True)
dataFrame_ohlc['Date'] = dataFrame_ohlc['Date'].map(mdates.date2num)

print(dataFrame_ohlc.head())
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
ax1.xaxis_date()

candlestick_ohlc(ax1, dataFrame_ohlc.values, width=2, colorup='g')
ax2.fill_between(dataFrame_volume.index.map(mdates.date2num), dataFrame_volume.values, 0)

# ax1.plot(dataFrame.index, dataFrame['Adj Close'])
# ax1.plot(dataFrame.index, dataFrame['100ma'])
# ax2.bar(dataFrame.index, dataFrame['Volume'])

plt.show()