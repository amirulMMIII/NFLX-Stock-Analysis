import pandas as pd
import plotly.graph_objects as go
import os

def create_chart():
    # 1. Tentukan laluan data processed
    data_path = os.path.join('data', 'processed', 'nflx_processed.csv')
    
    if not os.path.exists(data_path):
        print(f"❌ Ralat: Fail {data_path} tidak dijumpai! Sila jalankan stock_engine.py dahulu.")
        return

    # 2. Baca data
    df = pd.read_csv(data_path)
    
    # Pastikan kolum Date dalam format datetime
    df['Date'] = pd.to_datetime(df.index) 

    # 3. Bina Graf Candlestick
    fig = go.Figure()

    # Tambah Candlestick
    fig.add_trace(go.Candlestick(
        x=df['Date'],
        open=df['Open'], high=df['High'],
        low=df['Low'], close=df['Close'],
        name='Market Data'
    ))

    # Tambah Moving Average 50 (Garis Biru)
    fig.add_trace(go.Scatter(x=df['Date'], y=df['MA50'], 
                             line=dict(color='blue', width=1.5), 
                             name='MA50 (Short Term)'))

    # Tambah Moving Average 200 (Garis Merah)
    fig.add_trace(go.Scatter(x=df['Date'], y=df['MA200'], 
                             line=dict(color='red', width=1.5), 
                             name='MA200 (Long Term)'))

    # 4. Kemaskini Layout
    fig.update_layout(
        title='Netflix (NFLX) Stock Analysis - Interactive Chart',
        yaxis_title='Stock Price (USD)',
        xaxis_title='Date',
        template='plotly_dark', # Tema gelap yang profesional
        xaxis_rangeslider_visible=False
    )

    # 5. Simpan dan Papar
    output_path = os.path.join('results', 'nflx_chart.html')
    fig.write_html(output_path)
    print(f"✅ Graf berjaya dijana! Sila buka: {output_path}")
    fig.show()

if __name__ == "__main__":
    create_chart()