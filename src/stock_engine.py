import yfinance as yf
import pandas as pd
import os
import numpy as np

def run_stock_pipeline(ticker='NFLX'):
    print(f"🚀 Memulakan Pipeline untuk: {ticker}")

    # 1. MUAT TURUN DATA (RAW)
    print("📡 Mendapatkan data dari Yahoo Finance...")
    data = yf.download(ticker, period="5y")
    
    if data.empty:
        print("❌ Gagal: Tiada data ditemui.")
        return

    # Tentukan laluan simpan RAW
    raw_path = os.path.join('data', 'raw', f'{ticker.lower()}_raw.csv')
    data.to_csv(raw_path)
    print(f"✅ Data MENTAH disimpan di: {raw_path}")

    # 2. PROSES DATA (CLEANING & ENGINEERING)
    print("🧹 Membersihkan dan memproses data...")
    df = data.copy()
    
    # Buat pengiraan teknikal
    df['Daily_Return'] = df['Close'].pct_change()
    df['MA50'] = df['Close'].rolling(window=50).mean()
    df['MA200'] = df['Close'].rolling(window=200).mean()
    
    # Buang baris kosong (NaN) hasil dari rolling/pct_change
    df_cleaned = df.dropna()

    # Tentukan laluan simpan PROCESSED
    processed_path = os.path.join('data', 'processed', f'{ticker.lower()}_processed.csv')
    df_cleaned.to_csv(processed_path)
    print(f"✅ Data BERSIH disimpan di: {processed_path}")

    print(f"\n✨ Analisis selesai untuk {ticker}!")
    print(f"--- Sila semak folder 'data/raw' dan 'data/processed' ---")

if __name__ == "__main__":
    # Jalankan pipeline
    run_stock_pipeline('NFLX')