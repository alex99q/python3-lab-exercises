from datetime import datetime
import pytz

european_cities = ("Sofia", "Berlin", "London", "Moscow", "Paris", "Rome")

for city in european_cities:
    tz = pytz.timezone("Europe/" + city)
    city_datetime = datetime.now(tz).strftime("%H:%M:%S %d-%m-%Y")
    print("The current time in {} is: {}".format(city, city_datetime))