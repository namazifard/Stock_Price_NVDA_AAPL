import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App by Danial Namazifard

Shown are the stock **closing price** and ***volume*** of Apple and Nvidia!

""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbolApple = 'AAPL'
#get data on this ticker
tickerDataApple = yf.Ticker(tickerSymbolApple)
#get the historical prices for this ticker
tickerDfApple = tickerDataApple.history(period='1d', start='2010-6-20', end='2024-6-20')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

# tickerSymbolNvidia = 'NVDA'
# #get data on this ticker
# tickerDataNvidia = yf.Ticker(tickerSymbolNvidia)
# #get the historical prices for this ticker
# tickerDfNvidia = tickerDataNvidia.history(period='1d', start='2010-6-20', end='2024-6-20')
# # Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
# Apple
## Closing Price
""")
st.line_chart(tickerDfApple.Close)

st.write("""
## Volume Price
""")
st.line_chart(tickerDfApple.Volume)

# st.write("""
# # NVIDIA
# ## Closing Price
# """)
# st.line_chart(tickerDfNvidia.Close)

# st.write("""
# ## Volume Price
# """)
# st.line_chart(tickerDfNvidia.Volume)