import numpy as np
import pandas as pd
import pandas_datareader.tiingo as tiingo
import matplotlib.pyplot as plt
%matplotlib inline
import datetime
import plotly.graph_objects as go

tKey = 'a16a1f832f5463e822c405a65074dabe1c4895d9'

# last trade day from previous year
# TODO: auto calculate
dStrLastYearClose = '12/31/2018'
dMarketBottom = '03/23/2020'

# get the current date
d = datetime.datetime.today()
# convert to string format
dStrToday = d.strftime('%m/%d/%Y')
dStrYearStart = d.strftime('01/01/%Y')

# tickers of all peers
peers = ['CRZO','CDEV','DNR','LPI','OAS','PDCE','PE','RRC','SM','SWN','WLL','WPX','XEC']
#gold tickers
gold = ['GOLD', 'AEM', 'NEM', 'AUY', 'KGC', 'FNV', 'KL', 'GDX']

# fetch the stock data
dr = tiingo.TiingoDailyReader(symbols=gold, start=dMarketBottom, end=dStrToday, api_key=tKey)
df = dr.read()
dr.close()

# show some stats on the data
df.describe()



# filter data down to adjusted close price
df_close = df.loc[gold,['adjClose']]

df_close.head()

# pivot the data
df_pivot = pd.pivot_table(df_close, index='date', columns='symbol',values="adjClose")

df_pivot.head(10)



# Calculate YTD performance
perf_ytd = (df_pivot / df_pivot.iloc[0,:]) - 1

perf_ytd

perf_ytd.plot(title='Gold YTD Performance', figsize=(20,10))