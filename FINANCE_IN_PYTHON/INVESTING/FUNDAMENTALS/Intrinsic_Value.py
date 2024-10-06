import yfinance as yf

def intrinsic_value(ticker):
    stock = yf.Ticker(ticker)
    free_cash_flow = stock.get_cashflow().iloc[0]
    capex = stock.get_cashflow().iloc[1]
    wacc = 0.12
    growth_rate = 0.10
    terminal_value = (free_cash_flow * (1 + growth_rate)) / (wacc - growth_rate)
    present_value = terminal_value / (1 + wacc)**6
    for i in range(1, 6):
        present_value += (free_cash_flow / (1 + wacc)**i)
    return present_value

ticker = "MSFT"
intrinsic_value_per_share = intrinsic_value(ticker) / 743000000000
print("The intrinsic value of", ticker, "is", intrinsic_value(ticker))
print("The intrinsic value per share is", intrinsic_value_per_share)
