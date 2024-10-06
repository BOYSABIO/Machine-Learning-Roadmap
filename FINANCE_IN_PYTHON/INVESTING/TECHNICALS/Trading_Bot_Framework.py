import yfinance as yf
import pandas as pd

# Must be within the past 60 days
dataF = yf.download("CRWD", start = "2024-1-1", end = "2024-1-10", interval = "15m")
dataF.iloc[-1:,:]
dataF.Open.iloc


# This can be modified depending on the strategy
def signal_generator(df):
    # Opening / closing price of candle
    open = df.Open.iloc[-1]
    close = df.Close.iloc[-1]
    # Opening / closing price of previous candle
    previous_open = df.Open.iloc[-2]
    previous_close = df.Close.iloc[-2]

    # Bearish Pattern
    if (open > close and previous_open < previous_close and 
        close < previous_open and open >= previous_close):
        return 1
    
    # Bullish Pattern
    elif (open < close and previous_open > previous_close and 
          close > previous_open and open <= previous_close):
        return 2
    
    # No clear pattern
    else:
        return 0
    
signal = []
signal.append(0)
for i in range(1, len(dataF)):
    df = dataF[i-1:i+1]
    signal.append(signal_generator(df))

# signal_generator(data)
dataF["signal"] = signal
print(dataF)
print(dataF.signal.value_counts())

print()
print(dataF.loc[dataF.signal == 1])
print()
print(dataF.loc[dataF.signal == 2])
