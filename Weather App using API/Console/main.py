# ----- Weather App Using API -----

# Requests Module
import requests

# Title
print("\n -------- Welcome to Weather App --------\n")

# City Name & API Key & URL
try:
    while True:
               city_name = input("Enter City Name: ")
               API_KEY = "9b79470a00144c322ffe1422b9e54079"
               URL = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"

               response = requests.get(URL)
               if response.status_code == 200:
                   print(f"\n✅ Weather data for {city_name} fetched successfully.")
                   data = response.json()
                   name = data["name"]
                   desc = data["weather"][0]["description"]
                   temp = data["main"]["temp"]
                   wind = data["wind"]["speed"]
                   humidity = data["main"]["humidity"]
                   clouds = data["clouds"]["all"]
                   lat = data["coord"]["lat"]
                   lon = data["coord"]["lon"]

                   print(f"\nWeather in {city_name}:\n")
                   print(f"City Name: {name}")
                   print(f"Coordinates: ({lat}, {lon})")
                   print(f"Temperature: {temp}°C")
                   print(f"Condition: {desc.title()}")
                   print(f"Humidity: {humidity}%")
                   print(f"Clouds: {clouds}%")
                   print(f"Wind: {wind}%\n")
               else:
                   print(f"\nError: {response.json().get('message', 'Unable to fetch Weather. Sorry...')}\n")

except KeyboardInterrupt:
                         print("\n\nExiting... Bye")
