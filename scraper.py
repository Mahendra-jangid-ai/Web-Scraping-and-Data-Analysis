import yfinance as yf
import pandas as pd


def get_stock_data(ticker="TCS.NS", period="1mo", interval="1d"):
    """Fetch historical stock data from Yahoo Finance"""
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period, interval=interval)
    return hist.reset_index()


def get_stock_info(ticker="TCS.NS"):
    """Fetch company info & current market data"""
    stock = yf.Ticker(ticker)
    return stock.info