import yfinance as yf
import pandas as pd
import os

def run_stock_pipeline(ticker='NFLX'):
    print(f"📡 [ADVANCED MODE] Mengambil data Intraday untuk: {ticker}")

    # 1. Ambil data 1 minit (Paling pantas di yfinance)
    # Nota: yfinance benarkan data 1m hanya untuk 7 hari terakhir sahaja
    data = yf.download(ticker, period="1d", interval="1m")
    
    if data.empty:
        print("❌ Ralat: Gagal mengambil data realtime.")
        return

    # Simpan RAW
    raw_path = os.path.join('data', 'raw', f'{ticker.lower()}_live.csv')
    data.to_csv(raw_path)

    # 2. ADVANCED ENGINEERING (Setara MooMoo)
    df = data.copy()
    
    # RSI (Indikator Overbought/Oversold)
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))

    # Bollinger Bands (Indikator Volatiliti)
    df['MA20'] = df['Close'].rolling(window=20).mean()
    df['STD20'] = df['Close'].rolling(window=20).std()
    df['Upper_Band'] = df['MA20'] + (df['STD20'] * 2)
    df['Lower_Band'] = df['MA20'] - (df['STD20'] * 2)

    # Simpan PROCESSED
    processed_path = os.path.join('data', 'processed', f'{ticker.lower()}_live_processed.csv')
    df.dropna().to_csv(processed_path)
    print(f"✅ Data Intraday & Indikator MooMoo-Style siap!")

if __name__ == "__main__":
    run_stock_pipeline('NFLX')