# ----- Weather App Using API -----

import requests

print("\n -------- Welcome to Weather App --------\n")

# API Key
API_KEY = "9b79470a00144c322ffe1422b9e54079"

def get_weather(city_name):
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        name = data["name"]
        desc = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        wind = data["wind"]["speed"]
        humidity = data["main"]["humidity"]
        clouds = data["clouds"]["all"]
        lat = data["coord"]["lat"]
        lon = data["coord"]["lon"]

        print(f"\n✅ Weather data for {city_name} fetched successfully.\n")
        print(f"City Name: {name}")
        print(f"Coordinates: ({lat}, {lon})")
        print(f"Temperature: {temp}°C")
        print(f"Condition: {desc.title()}")
        print(f"Humidity: {humidity}%")
        print(f"Clouds: {clouds}%")
        print(f"Wind: {wind}%\n")
    else:
        print(f"\nError: {response.json().get('message', 'Unable to fetch Weather. Sorry...')}\n")


try:
    # Step 1: Get current city using IP
    location = requests.get("https://ipinfo.io/json").json()
    current_city = location.get("city")

    if current_city:
        print(f"🌍 Detecting your current location: {current_city}")
        get_weather(current_city)
    else:
        print("⚠️ Could not detect location automatically.")

    # Step 2: User can search for other cities
    while True:
        city_name = input("Enter City Name (or type 'exit' to quit): ")
        if city_name.lower() == "exit":
            break
        get_weather(city_name)

except KeyboardInterrupt:
    print("\n\nExiting... Bye")
