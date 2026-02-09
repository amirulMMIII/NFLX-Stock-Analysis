import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

def create_chart():
    df = pd.read_csv(os.path.join('data', 'processed', 'nflx_live_processed.csv'))
    
    # Cipta 2 baris graf (Satu untuk Candlestick, satu untuk RSI)
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
                       vertical_spacing=0.1, subplot_titles=('NFLX Price & Bollinger Bands', 'RSI'),
                       row_width=[0.3, 0.7])

    # 1. Candlestick & Bollinger Bands (Row 1)
    fig.add_trace(go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'], name='Price'), row=1, col=1)
    fig.add_trace(go.Scatter(x=df.index, y=df['Upper_Band'], line=dict(color='rgba(173, 216, 230, 0.5)'), name='Upper Band'), row=1, col=1)
    fig.add_trace(go.Scatter(x=df.index, y=df['Lower_Band'], line=dict(color='rgba(173, 216, 230, 0.5)'), fill='tonexty', name='Lower Band'), row=1, col=1)

    # 2. RSI (Row 2)
    fig.add_trace(go.Scatter(x=df.index, y=df['RSI'], line=dict(color='yellow'), name='RSI'), row=2, col=1)
    fig.add_hline(y=70, line_dash="dash", line_color="red", row=2, col=1) # Overbought
    fig.add_hline(y=30, line_dash="dash", line_color="green", row=2, col=1) # Oversold

    fig.update_layout(height=800, template='plotly_dark', title='NFLX ADVANCED REALTIME DASHBOARD', xaxis_rangeslider_visible=False)
    
    fig.write_html('index.html') # Simpan terus untuk GitHub Pages
    fig.show()

if __name__ == "__main__":
    create_chart()