import os
import sys
from src.stock_engine import run_stock_pipeline
from src.visualize import create_chart

def start_mission():
    print("="*40)
    print("   NFLX STOCK ANALYSIS - MASTER SYSTEM   ")
    print("="*40)

    try:
        # Fasa 1: Data & Processing
        print("\n[PHASE 1]: Memuat turun dan memproses data...")
        run_stock_pipeline('NFLX')

        # Fasa 2: Visualization
        print("\n[PHASE 2]: Menjana graf interaktif...")
        create_chart()

        print("\n" + "="*40)
        print("✅ MISI SELESAI: Dashboard sedia untuk disemak.")
        print("="*40)

    except Exception as e:
        print(f"\n❌ RALAT SISTEM: {e}")

if __name__ == "__main__":
    start_mission()