import os
import requests, zipfile, io

# Set the root folder name
PROJECT_ROOT = "bike_rental_forecast"

# Full folder structure to create
folders = [
    f"{PROJECT_ROOT}/data",
    f"{PROJECT_ROOT}/notebooks",
    f"{PROJECT_ROOT}/models",
    f"{PROJECT_ROOT}/outputs"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

print("Folder structure created inside", PROJECT_ROOT)

# Download and extract dataset into data folder
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00275/Bike-Sharing-Dataset.zip"
response = requests.get(url)
with zipfile.ZipFile(io.BytesIO(response.content)) as z:
    z.extractall(f"{PROJECT_ROOT}/data")

print("Dataset downloaded and extracted to data/")
