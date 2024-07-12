# webscrapping
# Libraries for web scrapping
# Request, BeautifulSoup, lxml, scrapy, selenium
# API Keys
# Exercises, openweathermap.org
import requests
from bs4 import BeautifulSoup
import csv
import json

# Step 2: Fetch the web pages
api_key = "7700f1ad62b8cffdcc29d51c5424005f"
city = 'Kampala'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}' 

response = requests.get(url)
weather_data = response.json()

# Step 3: Find the specific data
data = [{
    'city': weather_data['name'],
    'temperature': weather_data['main']['temp'],
    'weather': weather_data['weather'][0]['description'],
    'humidity': weather_data['main']['humidity'],
    'pressure': weather_data['main']['pressure'],
    'wind_speed': weather_data['wind']['speed']
}]

# Step 4: Save the data to a CSV file
csv_file = 'weather_data.csv'
with open(csv_file, mode='w', newline='',encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames = ['city', 'temperature', 'weather', 'humidity', 'pressure', 'wind_speed'])
    writer.writeheader()
    for row in data:
        writer.writerow(row)

# Step 5: Save the data to a JSON file
json_file = 'weather_data.json'
with open(json_file, mode='w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
    
# Step 6: Save successfully to csv and json format
print(f'Data saved successfully to {csv_file} and {json_file} format!')