import pandas as pd
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt

# Download list of SP500 ticker from Wikipedia and downlaod price data from Yahoo Finance
sp500 = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies", attrs = {'id': 'constituents'})[0]
price_data = yf.download(sp500['Symbol'].to_list(), start="2021-01-01", end="2021-4-28", auto_adjust=True)

# Correlation of closing prices
corr = price_data['Close'].corr().fillna(0)

# Plot covariance matrix
plt.figure(figsize=(16, 16))
sns.heatmap(round(corr,2), cmap="RdBu", vmax=1.0, vmin=-1.0, center=0, xticklabels=False, yticklabels=False, cbar=False)
plt.savefig("img/corr_sp500.png")
plt.show()