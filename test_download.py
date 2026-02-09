import yfinance as yf
import os

# 1. Tentukan lokasi simpan
path_mentah = "data/raw/nflx_stock.csv"

# 2. Muat turun data
print("Sedang mengambil data dari pasaran...")
df = yf.download("NFLX", period="1mo") # Ambil data 1 bulan

# 3. Simpan ke dalam folder RAW
df.to_csv(path_mentah)
print(f"Berjaya! Data mentah disimpan di: {path_mentah}")