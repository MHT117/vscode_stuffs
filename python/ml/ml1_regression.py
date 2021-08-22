import pandas as pd
import quandl 
#df = data frame (A Data frame is a two-dimensional data structure)
#df = quandl.get('BATS/EDGA_XLTY')
df = quandl.get('WIKI/GOOGL')
df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
df['HL_PCT'] = (df['Adj. High']- df['Adj. Close']) / df['Adj. Open'] * 100
df['PCT_change'] = (df['Adj. Close']- df['Adj. Open']) / df['Adj. Open'] * 100

print(df.head())
