import os

# 1. Tentukan Direktori Utama (Base Directory)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 2. DEFINISIKAN PEMBOLEHUBAH (Selesaikan ralat UndefinedVariable)
RAW_DATA = os.path.join(BASE_DIR, 'data', 'raw')
PROCESSED_DATA = os.path.join(BASE_DIR, 'data', 'processed')
RESULTS_DIR = os.path.join(BASE_DIR, 'results')

# 3. SENARAI FOLDER UNTUK DICIPTA
folders_to_create = [RAW_DATA, PROCESSED_DATA, RESULTS_DIR]

# 4. LOGIK PENCIPTAAN FOLDER (Robust)
for folder in folders_to_create:
    try:
        if os.path.exists(folder):
            if not os.path.isdir(folder):
                # Jika ada fail yang menghalang dengan nama yang sama, buang ia
                print(f"CORE: Mengesan fail penghalang di {folder}. Menghapuskan...")
                os.remove(folder)
                os.makedirs(folder, exist_ok=True)
            else:
                print(f"CORE: Folder sudah wujud -> {folder}")
        else:
            os.makedirs(folder, exist_ok=True)
            print(f"CORE: Folder dicipta -> {folder}")
    except Exception as e:
        print(f"WARNING: Isu akses pada {folder}: {e}")