# Meteocat Tools 

Meteocat tools is a Python script for interacting with Meteocat API data. Mainly to determine which areas meet the proper conditions to grow certain plant species. 

## Prerequisites

Request an API key from Meteocat [here](https://apidocs.meteocat.gencat.cat/section/informacio-general/plans-i-registre/)


## Usage

```python
# run command
source venv/bin/activate
pip3 install requests
python3 meteocat.py

# returns
Daily Weather Summary:
2025-10-27 → Rainfall: 0 mm | Max Temp: 19.1°C | Min Temp: 6.7°C 
2025-10-26 → Rainfall: 5.5 mm | Max Temp: 18.8°C | Min Temp: 8.5°C (!!)
2025-10-25 → Rainfall: 0.5 mm | Max Temp: 23.1°C | Min Temp: 11.9°C 
2025-10-24 → Rainfall: 0 mm | Max Temp: 21.7°C | Min Temp: 8.4°C 
2025-10-23 → Rainfall: 0 mm | Max Temp: 25.1°C | Min Temp: 12°C 
2025-10-22 → Rainfall: 0 mm | Max Temp: 26.4°C | Min Temp: 13°C 
2025-10-21 → Rainfall: 0 mm | Max Temp: 25.4°C | Min Temp: 10.7°C 
2025-10-20 → Rainfall: 1.5 mm | Max Temp: 24.6°C | Min Temp: 13.1°C 
2025-10-19 → Rainfall: 0 mm | Max Temp: 23.9°C | Min Temp: 12.1°C 
2025-10-18 → Rainfall: 0.1 mm | Max Temp: 23.4°C | Min Temp: 11.8°C 
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

Not under any liscense. Free to use and distribute.
