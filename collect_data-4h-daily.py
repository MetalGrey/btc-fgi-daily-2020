import requests
import pandas as pd
from datetime import datetime


url = "https://api.coingecko.com/api/v3/coins/bitcoin/ohlc"
params = {
    "vs_currency": "usd",
    "days": "30"
}

response = requests.get(url, params=params)
data = response.json()
df_new = pd.DataFrame(data, columns=["timestamp", "open", "high", "low", "close"])
df_new = df_new[["timestamp", "open", "close", "high", "low"]]
df_new["timestamp"] = pd.to_datetime(df_new["timestamp"], unit="ms")

df_existing = pd.read_csv("datasets/btc_with_fgi_4h.csv", parse_dates=["timestamp"])

df_combined = pd.concat([df_new, df_existing], ignore_index=True)
df_combined.drop_duplicates(subset=["timestamp"], inplace=True)
df_combined.sort_values("timestamp", ascending=False, inplace=True) 

url = "https://api.alternative.me/fng/?limit=20&format=json"
response = requests.get(url)
data = response.json()["data"]
fear_df = pd.DataFrame(data)
fear_df['timestamp'] = pd.to_datetime(fear_df['timestamp'], unit='s')
fear_df['value'] = fear_df['value'].astype(int)

df_combined["date"] = df_combined["timestamp"].dt.date
fear_df["date"] = fear_df["timestamp"].dt.date

latest_fgi_dates = fear_df["date"].unique()[:20]
fear_df_latest = fear_df[fear_df["date"].isin(latest_fgi_dates)]

df_combined = df_combined.copy()
df_combined.loc[df_combined["date"].isin(latest_fgi_dates), ["Fear & Greed Index", "Fear & Greed Classification"]] = None

df_combined = pd.merge(
    df_combined,
    fear_df_latest[["date", "value", "value_classification"]],
    on="date",
    how="left"
)

df_combined["Fear & Greed Index"] = df_combined["value"].combine_first(df_combined["Fear & Greed Index"])
df_combined["Fear & Greed Classification"] = df_combined["value_classification"].combine_first(df_combined["Fear & Greed Classification"])
df_combined = df_combined.drop(columns=["date", "value", "value_classification"])
df_combined = df_combined.sort_values(by="timestamp", ascending=False).reset_index(drop=True)
df_combined.to_csv("datasets/btc_with_fgi_4h.csv", index=False)

