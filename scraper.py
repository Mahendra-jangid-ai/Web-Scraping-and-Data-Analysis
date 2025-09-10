import yfinance as yf
import pandas as pd


def get_stock_data(ticker="TCS.NS", period="1mo", interval="1d"):
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period, interval=interval)
    return hist.reset_index()


def get_stock_info(ticker="TCS.NS"):
    stock = yf.Ticker(ticker)
    return stock.info