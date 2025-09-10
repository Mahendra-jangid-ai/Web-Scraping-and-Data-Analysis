# 📊 Stock Dashboard (Flask + yFinance + Chart.js)

A web-based stock analysis dashboard built with **Flask**, **yFinance**, **Pandas**, and **Chart.js**.  
It allows users to fetch **real-time stock data**, visualize price trends, and view key summary statistics.

🚀 **Live Demo**: [Stock Dashboard on Render](https://web-scraping-and-data-analysis.onrender.com)

---

## ✨ Features
- 🔎 Search for any stock by ticker symbol (e.g., `TCS.NS`, `INFY.NS`, `RELIANCE.NS`)  
- 📈 Interactive **line chart** of stock closing prices (last 1 month by default)  
- 📊 Summary analysis including:
  - Mean Close Price  
  - Max Close Price  
  - Min Close Price  
  - Latest Close Price  
  - Return % over selected period  
- 🌐 Live deployment on **Render**  

---

## 🛠️ Tech Stack
- **Backend**: Flask, yFinance, Pandas  
- **Frontend**: HTML, CSS, JavaScript, Chart.js  
- **Deployment**: Render  

---

## 📂 Project Structure
WEB-SCRAPING-AND-DATA-ANALYSIS/
│── static/
│ ├── app.js # Frontend logic (API calls + chart rendering)
│ ├── style.css # Styling
│
│── templates/
│ ├── index.html # Main frontend page
│
│── app.py # Flask backend (routes + APIs)
│── scraper.py # yFinance stock data functions
│── requirements.txt # Python dependencies
│── Procfile # For Render deployment (gunicorn)
│── README.md # Documentation



---

## ⚡ Installation (Run Locally)

1. Clone the repo:
   ```bash
   git clone https://github.com/Mahendra-jangid-ai/Web-Scraping-and-Data-Analysis.git
   cd Web-Scraping-and-Data-Analysis


python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)

pip install -r requirements.txt



