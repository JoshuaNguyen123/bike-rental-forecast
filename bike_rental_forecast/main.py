"""
bike_rental_forecast/main.py
Entry point:  python -m bike_rental_forecast.main
"""

from pathlib import Path
from .models.prophet_model import run_prophet_model   # ← relative import (PEP 328)

# --------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent        # .../bike_rental_forecast
DATA_PATH    = PROJECT_ROOT / "data" / "day.csv"
OUTPUT_PATH  = PROJECT_ROOT / "outputs" / "forecast_plot.png"
# --------------------------------------------------

def main() -> None:
    forecast = run_prophet_model(DATA_PATH, OUTPUT_PATH)
    print(forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail())

if __name__ == "__main__":
    main()
