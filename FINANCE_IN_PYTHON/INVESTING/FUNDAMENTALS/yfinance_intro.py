import yfinance as yf
import pandas as pd

getstockdata = yf.Ticker(input("Enter symbol: "))
print(getstockdata.history())
print(getstockdata.fast_info)
print()
print(getstockdata.fast_info.year_change)
print(getstockdata.major_holders)
print()

df = pd.DataFrame(getstockdata.history("10y"))
print(df.info())
print(df.describe())

print("Currency")
print(getstockdata.fast_info.currency)


print(df.loc[df.Dividends > 0.0])
print()

print(df.loc[df.High > 1900])