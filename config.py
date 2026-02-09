import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_DATA = os.path.join(BASE_DIR, 'data', 'raw')
PROCESSED_DATA = os.path.join(BASE_DIR, 'data', 'processed')
RESULTS_DIR = os.path.join(BASE_DIR, 'results')

# Pastikan folder wujud secara automatik
for folder in [RAW_DATA, PROCESSED_DATA, RESULTS_DIR]:
    os.makedirs(folder, exist_ok=True)