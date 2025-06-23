from prophet import Prophet
import pandas as pd
import matplotlib.pyplot as plt
import os

def run_prophet_model(data_path, output_path="outputs/forecast_plot.png"):
    # Load data
    df = pd.read_csv(data_path)
    df["dteday"] = pd.to_datetime(df["dteday"])

    # Rename columns for Prophet
    prophet_df = df[["dteday", "cnt"]].rename(columns={"dteday": "ds", "cnt": "y"})

    # Build model
    model = Prophet(daily_seasonality=True)
    model.fit(prophet_df)

    # Future dataframe
    future = model.make_future_dataframe(periods=30)  # forecast 30 days ahead
    forecast = model.predict(future)

    # Plot forecast
    fig = model.plot(forecast)
    plt.title("Prophet Forecast: Daily Bike Rentals")
    plt.savefig(output_path)
    plt.close()

    print(f"Forecast plot saved to {output_path}")
    return forecast
