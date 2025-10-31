## meteocat.py
import requests
import argparse
from datetime import datetime, timedelta
from config import METEOCAT_API_KEY  # Import the key from config.py


# Prompt user to choose a station
print("Choose a weather station (code):")
print("- Sant Sadurní d'Anoia (YO)")
print("- La Llacuna (XB)")
print("- Pujalt (YH)")
print("- Gisclareny (UI)")
print("- Castellar de n'Hug (MS)")
choice = input("Enter station code: ")

# Define a list of allowed station codes
station_codes = ["UI", "YH", "YO", "XB", "MS"]

# Check if the value exists
if choice.upper() in station_codes:
    station_code = choice.upper()
else:
    station_code = "YO"
    print("Invalid choice. Defaulting to Sant Sadurní d'Anoia (YO).")

# Configurations
base_url = 'https://api.meteo.cat/xema/v1'
start_date = datetime.today()
num_days = 10
daily_summary = []

# Loop through the last 10 days
for i in range(num_days):
    date = start_date - timedelta(days=i)
    date_str = date.strftime('%Y/%m/%d')
    url = f'{base_url}/estacions/mesurades/{station_code}/{date_str}'

    response = requests.get(url, headers={
        "Content-Type": "application/json",
        "X-Api-Key": METEOCAT_API_KEY
    })

    if response.status_code == 200:
        data = response.json()
        variables = data[0].get('variables', [])

        rainfall = 0.0
        max_temp = None
        min_temp = None

        for var in variables:
            code = var.get('codi')
            readings = var.get('lectures', [])

            if code == 35:  # Rainfall
                rainfall = sum(entry['valor'] for entry in readings)
            elif code == 40:  # Max temperature
                max_temp = max(entry['valor'] for entry in readings)
            elif code == 42:  # Min temperature
                min_temp = min(entry['valor'] for entry in readings)

        daily_summary.append((date.strftime('%Y-%m-%d'), rainfall, max_temp, min_temp))
    else:
        print(f"Failed to fetch data for {date_str}: {response.status_code}")
        daily_summary.append((date.strftime('%Y-%m-%d'), None, None, None))

# Output results
print("\nLast 10-day Weather Summary:")
print("-" * 50)
for day, rain, max_t, min_t in daily_summary:
    flag = ""
    if(rain > 5 and max_t < 25 and min_t > 0):
        flag = " (!!)"
    print(f"{day} → Rainfall: {rain if rain is not None else 'N/A'} mm | "
          f"Max Temp: {max_t if max_t is not None else 'N/A'}°C | "
          f"Min Temp: {min_t if min_t is not None else 'N/A'}°C {flag}")
