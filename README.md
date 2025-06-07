
# 📈 BTCUSDT 4h OHLC + Fear & Greed Index (from 2020-03-25)

This repository contains a clean and ready-to-use dataset of **Bitcoin (BTC/USDT)** 4-hour OHLC data enriched with the **Crypto Fear & Greed Index (FGI)** starting from **2020-03-25**.

It is ideal for time-series analysis, sentiment-based strategies, algorithmic trading, and machine learning tasks.

---

## 🗂 Dataset Overview

The dataset is stored as a CSV file and contains the following columns:

| Column                       | Description                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| ⏰ `timestamp`              | Start time of the 4-hour OHLC candle in UTC.                               |
| 🟢 `open`                  | BTC/USDT price at the beginning of the interval.                           |
| 🔴 `close`                 | BTC/USDT price at the end of the interval.                                 |
| 🔼 `high`                  | Highest BTC/USDT price during the interval.                                |
| 🔽 `low`                   | Lowest BTC/USDT price during the interval.                                 |
| 😨 `Fear & Greed Index`    | Daily sentiment score (0–100) from alternative.me API.                     |
| 📉 `Fear & Greed Classification` | Sentiment label (e.g., Extreme Fear, Fear, Neutral, Greed, Extreme Greed). |

---

## 📊 Example Usage (Python)

```python
import pandas as pd

df = pd.read_csv("datasets/btc_with_fgi_4h.csv", parse_dates=["timestamp"])
print(df.head())
```

You can use this dataset for:
- 📈 Time-series forecasting
- 🧠 Sentiment-based ML modeling
- 🤖 Crypto trading bots
- 📊 Data visualization

---

## 📅 Date Range

- **Start**: 2020-03-25  
- **Interval**: 4 hours  
- **Updated**: Continuously (latest Fear & Greed Index merged)

---

## 📡 Data Sources

- [CoinGecko API](https://www.coingecko.com/en/api/documentation) – for OHLC data  
- [Alternative.me API](https://alternative.me/crypto/fear-and-greed-index/) – for Fear & Greed Index

---

## 📄 License

This dataset is released under the **CC0: Public Domain**.  

---

## 💡 Contributing

Pull requests and improvements are welcome! Feel free to submit issues or enhancements.

---

## 🙌 Acknowledgements

- Data collected using public APIs from [CoinGecko](https://www.coingecko.com/) and [Alternative.me](https://alternative.me/crypto/).
