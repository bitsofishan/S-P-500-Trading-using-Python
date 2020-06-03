import datetime as dt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import pandas_datareader.data as web
from mpl_finance import candlestick_ochl
import matplotlib.dates as mdates
style.use('ggplot')

#use this for getting the data then comment it out
'''start=dt.datetime(2000,1,1)
end=dt.datetime(2016,12,31)
#lets scrape the data from yahoo for apple
df=web.DataReader('TSLA','yahoo',start,end)
print(df.head())'''

#lets save the data to a csv
df.to_csv('tsla.csv')
df=pd.read_csv('tsla.csv',parse_dates=True,index_col=0)
df.head()

# if you want to visulaize the data,uncomment the below two lines
'''df['Adj Close'].plot()
plt.show()'''
#ading a column for moving averagge using last 100 days
#df['100ma'] = df['Adj Close'].rolling(window=100,min_periods=0).mean()
df_ohlc=df['Adj Close'].resample('10D').ohlc()
df_volume=df['Volume'].resample('10D').sum
df_ohlc.reset_index(inplace=True)
df_ohlc['Date']=df_ohlc['Date'].map(mdates.date2num)




#lets plot and see the 100ma
ax1=plt.subplot2grid((6,1),(0,0),rowspan=5,colspan=1)
ax2=plt.subplot2grid((6,1),(5,0),rowspan=1,colspan=1,sharex=ax1)
ax1.xaxis_date()
candlestick_ochl(ax1,df_ohlc.values,width=2,colorup='g')
ax2.fill_between(df_volume.index.map(mdates.date2num),df_volume.values,0)
plt.show()

