from flask import Flask, jsonify, request, render_template
from scraper import get_stock_data, get_stock_info
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/stock")
def stock_data():
    ticker = request.args.get("ticker", "TCS.NS")
    period = request.args.get("period", "1mo")
    interval = request.args.get("interval", "1d")
    try:
        df = get_stock_data(ticker, period, interval)
        df['Date'] = df['Date'].astype(str)
        return df.to_dict(orient="records")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/stock/summary")
def stock_summary():
    ticker = request.args.get("ticker", "TCS.NS")
    period = request.args.get("period", "1mo")
    interval = request.args.get("interval", "1d")
    try:
        df = get_stock_data(ticker, period, interval)
        summary = {
            "mean_close": round(df["Close"].mean(), 2),
            "max_close": round(df["Close"].max(), 2),
            "min_close": round(df["Close"].min(), 2),
            "latest_close": round(df["Close"].iloc[-1], 2),
            "return_%": round(((df["Close"].iloc[-1] / df["Close"].iloc[0]) - 1) * 100, 2)
        }
        return jsonify(summary)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
