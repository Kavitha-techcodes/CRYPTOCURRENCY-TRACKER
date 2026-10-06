# Cryptocurrency Price Tracker

## 📌 Project Overview

The **Cryptocurrency Price Tracker** is a Python-based web scraping project that collects real-time cryptocurrency information from **CoinMarketCap**.

The project uses **Selenium WebDriver** to load the dynamic CoinMarketCap website and extract cryptocurrency details such as:

- Cryptocurrency Name
- Current Price
- 24-Hour Price Change
- Market Capitalization

The collected data is stored in a CSV file with timestamps and displayed through a **Streamlit dashboard**.

---

## 🎯 Objectives

The main objectives of this project are:

1. To collect real-time cryptocurrency prices.
2. To scrape dynamically loaded web pages using Selenium.
3. To retrieve information about the top 10 cryptocurrencies.
4. To store cryptocurrency data in CSV format.
5. To maintain historical data using timestamps.
6. To filter cryptocurrencies based on price.
7. To identify the highest 24-hour gainer.
8. To provide a dashboard for viewing cryptocurrency data.
9. To support portfolio tracking and historical price analysis.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Main programming language |
| Selenium | Web scraping |
| Chrome WebDriver | Browser automation |
| webdriver-manager | Automatic ChromeDriver management |
| Pandas | Data processing and CSV handling |
| Streamlit | Dashboard |
| CSV | Data storage |

---

## 📂 Project Structure

```text
Cryptocurrency_Price_Tracker/
│
├── main.py
├── scraper.py
├── filters.py
├── dashboard.py
├── requirements.txt
├── README.md
│
└── data/
    └── crypto_data.csv
