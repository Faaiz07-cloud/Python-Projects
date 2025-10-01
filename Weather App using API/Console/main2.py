# ----- Weather App Using API -----

# Requests Module
import requests

# Title
print("\n -------- Welcome to Weather App --------")

# City Name & API Key & URL
try:
    while True:
               city_name = input("\nEnter City Name: ")
               API_KEY = "9b79470a00144c322ffe1422b9e54079"
               URL = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_KEY}&units=metric"

               response = requests.get(URL)
               if response.status_code == 200:
                   print(f"\n✅ Weather data for {city_name} fetched successfully.")
                   data = response.json()
                   print("\n------ Weather Report ------\n")
                   print(f"City Name      : {data['city']['name']}")
                   print(f"Country        : {data['city']['country']}")
                   print(f"Timezone       : {data['city']['timezone']}")
                   print(f"Population     : {data['city']['population']}")
                   print("-" * 30)

                   for i, item in enumerate(data["list"][:5]):
                       print(f"\nRecord {i + 1}")
                       print(f"Date & Time    : {item['dt_txt']}")
                       print(f"Temperature    : {item['main']['temp']} °C")
                       print(f"Feels Like     : {item['main']['feels_like']} °C")
                       print(f"Humidity       : {item['main']['humidity']} %")
                       print(f"Weather        : {item['weather'][0]['description']}")
                       print(f"Rain Chance    : {item.get('pop', 0) * 100} %")
                       print(f"Wind Speed     : {item['wind']['speed']} m/s")
                       print("-" * 30)
               else:
                   print(f"\nError: {response.json().get('message', 'Unable to fetch Weather. Sorry...')}\n")

except KeyboardInterrupt:
                         print("\n\nExiting... Bye")
