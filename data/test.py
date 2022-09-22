import yfinance as yf
data = yf.download("AAPL", start="2022-09-20", end="2022-09-21", interval="1m")
print(data)
