# 📈 NFLX Real-Time Analytics & Technical Prediction
![Python](https://img.shields.io/badge/Python-3.9+-blue.svg?style=for-the-badge&logo=python)
![Plotly](https://img.shields.io/badge/Plotly-Interactive-orange.svg?style=for-the-badge&logo=plotly)
![Status](https://img.shields.io/badge/Status-Advanced-brightgreen.svg?style=for-the-badge)

Sistem pemantauan saham Netflix (NFLX) secara *real-time* (intraday) yang dilengkapi dengan algoritma pengiraan indikator teknikal untuk ramalan momentum pasaran.



## 🌟 Ciri Utama (Advanced Features)
* **Intraday Live Data**: Mengambil data pergerakan harga setiap 1 minit terus dari pasaran global.
* **Bollinger Bands Analysis**: Mengukur volatiliti pasaran untuk mengenal pasti zon *breakout* atau *reversal*.
* **RSI (Relative Strength Index)**: Menghitung momentum untuk mengesan keadaan *Overbought* (>70) atau *Oversold* (<30).
* **Automated Pipeline**: Dari pengambilan data mentah, pembersihan, sehingga penjanaan graf hanya dengan satu arahan.
* **Cloud Deployment**: Dashboard interaktif dihoskan secara automatik melalui GitHub Pages.

## 📊 Indikator Prediksi
Projek ini menggunakan kombinasi dua indikator utama untuk membantu keputusan dagangan:
1.  **Bollinger Bands**: Membantu menentukan sama ada harga berada pada tahap tinggi atau rendah secara relatif.
2.  **RSI**: Digunakan untuk mengesahkan kekuatan trend harga bagi mengelakkan "false signals".

## 📂 Struktur Projek
```text
├── data/
│   ├── raw/          # Data intraday mentah (.csv)
│   └── processed/    # Data dengan pengiraan RSI & Bollinger Bands
├── src/
│   ├── stock_engine.py  # Enjin pemprosesan data & indikator
│   └── visualize.py     # Enjin penjanaan graf interaktif
├── results/          # Hasil visualisasi HTML
├── main.py           # Pusat kawalan utama (Master Script)
└── index.html        # Laman web utama untuk GitHub Pages