"""
https://www.weather.gov/
forecast.weather.gov
Type in Nashville TN and hit Go
Inspect the web page in chrome
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=36.16784000000007&lon=-86.77815999999996')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-body')
# print(week)

items = week.find_all(class_='tombstone-container')
# print(items[0])

# print(items[0].find(class_='period-name').get_text())
# print(items[0].find(class_='short-desc').get_text())
# print(items[0].find(class_='temp').get_text())

period_names = [item.find(class_='period-name').get_text() for item in items]
short_description = [item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]

# print(period_names)
# print(short_description)
# print(temperatures)

weather_info = pd.DataFrame(
    {
        'period': period_names,
        'short_description': short_description,
        'temperatures': temperatures,
     })

print(weather_info)
# weather_info.to_csv()
