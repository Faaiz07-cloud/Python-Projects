# ---------- Unit Converter ----------

# --- Length Conversion Menu ---
def length_conversion_menu():
    while True:
        print("\n--- Length Conversion ---")
        print("""
        1. Meters → Feet
        2. Feet → Meters
        3. Meters → Inches
        4. Inches → Meters
        5. Kilometers → Meters
        6. Meters → Kilometers
        7. Centimeters → Inches
        8. Inches → Centimeters
        0. Back to Main Menu
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            print("\nMeters → Feet")
            meters = float(input("Enter value in meters: "))
            feet = meters * 3.28084
            print(f"\n{meters} meters = {feet:.2f} feet")

        elif choice == "2":
            print("\nFeet → Meters")
            feet = float(input("Enter value in feet: "))
            meters = feet / 3.28084
            print(f"\n{feet} feet = {meters:.2f} meters")

        elif choice == "3":
            print("\nMeters → Inches")
            meters = float(input("Enter value in meters: "))
            inches = meters * 39.3701
            print(f"\n{meters} meters = {inches:.2f} inches")

        elif choice == "4":
            print("\nInches → Meters")
            inches = float(input("Enter value in inches: "))
            meters = inches / 39.3701
            print(f"\n{inches} inches = {meters:.4f} meters")

        elif choice == "5":
            print("\nKilometers → Meters")
            km = float(input("Enter value in kilometers: "))
            meters = km * 1000
            print(f"\n{km} kilometers = {meters:.2f} meters")

        elif choice == "6":
            print("\nMeters → Kilometers")
            meters = float(input("Enter value in meters: "))
            km = meters / 1000
            print(f"\n{meters} meters = {km:.4f} kilometers")

        elif choice == "7":
            print("\nCentimeters → Inches")
            cm = float(input("Enter value in centimeters: "))
            inches = cm / 2.54
            print(f"\n{cm} cm = {inches:.2f} inches")

        elif choice == "8":
            print("\nInches → Centimeters")
            inches = float(input("Enter value in inches: "))
            cm = inches * 2.54
            print(f"\n{inches} inches = {cm:.2f} cm")

        elif choice == "0":
            print("\nReturning to Main Menu...")
            main()

        else:
            print("\n--- ⚠️ Invalid choice, please try again. ---\n")
            continue
# ---------------------------------------------------------

# --- Weight Conversion Menu ---
def weight_mass_conversion_menu():
    while True:
        print("\n--- Weight / Mass Conversion ---")
        print("""
         1. Kilograms → Pounds
         2. Pounds → Kilograms
         3. Grams → Kilograms
         4. Kilograms → Grams
         0. Back to Main Menu
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            print("\nKilograms → Pounds")
            kg = float(input("Enter value in kilograms: "))
            pounds = kg * 2.20462
            print(f"\n{kg} kilograms = {pounds:.2f} pounds")

        elif choice == "2":
            print("\nPounds → Kilograms")
            pounds = float(input("Enter value in pounds: "))
            kg = pounds / 2.20462
            print(f"\n{pounds} pounds = {kg:.2f} kilograms")

        elif choice == "3":
            print("\nGrams → Kilograms")
            grams = float(input("Enter value in grams: "))
            kg = grams / 1000
            print(f"\n{grams} grams = {kg:.3f} kilograms")

        elif choice == "4":
            print("\nKilograms → Grams")
            kg = float(input("Enter value in kilograms: "))
            grams = kg * 1000
            print(f"\n{kg} kilograms = {grams:.0f} grams")

        elif choice == "0":
            print("\nReturning to Main Menu...")
            main()

        else:
            print("\n--- ⚠️ Invalid choice, please try again. ---\n")
            continue
# ---------------------------------------------------------

# --- Temperature Conversion Menu ---
def temperature_conversion_menu():
    while True:
        print("\n--- Temperature Conversion ---")
        print("""
         1. Celsius → Fahrenheit
         2. Fahrenheit → Celsius
         3. Celsius → Kelvin
         4. Kelvin → Celsius
         0. Back to Main Menu
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            print("\nCelsius → Fahrenheit")
            c = float(input("Enter temperature in Celsius: "))
            f = (c * 9 / 5) + 32
            print(f"\n{c} °C = {f:.2f} °F")

        elif choice == "2":
            print("\nFahrenheit → Celsius")
            f = float(input("Enter temperature in Fahrenheit: "))
            c = (f - 32) * 5 / 9
            print(f"\n{f} °F = {c:.2f} °C")

        elif choice == "3":
            print("\nCelsius → Kelvin")
            c = float(input("Enter temperature in Celsius: "))
            k = c + 273.15
            print(f"\n{c} °C = {k:.2f} K")

        elif choice == "4":
            print("\nKelvin → Celsius")
            k = float(input("Enter temperature in Kelvin: "))
            c = k - 273.15
            print(f"\n{k} K = {c:.2f} °C")

        elif choice == "0":
            print("\nReturning to Main Menu...")
            main()

        else:
            print("\n--- ⚠️ Invalid choice, please try again. ---\n")
            continue
# ---------------------------------------------------------

# --- Time Conversion Menu ---
def time_conversion_menu():
    while True:
        print("\n--- Time Conversion ---")
        print("""
          1. Hours → Minutes
          2. Minutes → Hours
          3. Seconds → Minutes
          4. Minutes → Seconds
          0. Back to Main Menu
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            print("\nHours → Minutes")
            hours = float(input("Enter time in hours: "))
            minutes = hours * 60
            print(f"\n{hours} hours = {minutes:.2f} minutes")

        elif choice == "2":
            print("\nMinutes → Hours")
            minutes = float(input("Enter time in minutes: "))
            hours = minutes / 60
            print(f"\n{minutes} minutes = {hours:.2f} hours")

        elif choice == "3":
            print("\nSeconds → Minutes")
            seconds = float(input("Enter time in seconds: "))
            minutes = seconds / 60
            print(f"\n{seconds} seconds = {minutes:.2f} minutes")

        elif choice == "4":
            print("\nMinutes → Seconds")
            minutes = float(input("Enter time in minutes: "))
            seconds = minutes * 60
            print(f"\n{minutes} minutes = {seconds:.2f} seconds")

        elif choice == "0":
           print("\nReturning to Main Menu...")
           main()

        else:
           print("\n--- ⚠️ Invalid choice, please try again. ---\n")
           continue
# ---------------------------------------------------------

# --- Area Conversion Menu ---
def area_conversion_menu():
    while True:
        print("\n--- Area Conversion ---")
        print("""
           1. Square Meters → Square Feet
           2. Square Feet → Square Meters
           3. Square Kilometers → Hectares
           4. Hectares → Square Kilometers
           5. Acres → Square Meters
           6. Square Meters → Acres
           0. Back to Main Menu
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            print("\nSquare Meters → Square Feet")
            sqm = float(input("Enter area in square meters: "))
            sqft = sqm * 10.7639
            print(f"\n{sqm} square meters = {sqft:.2f} square feet")

        elif choice == "2":
            print("\nSquare Feet → Square Meters")
            sqft = float(input("Enter area in square feet: "))
            sqm = sqft / 10.7639
            print(f"\n{sqft} square feet = {sqm:.2f} square meters")

        elif choice == "3":
            print("\nSquare Kilometers → Hectares")
            sqkm = float(input("Enter area in square kilometers: "))
            hectares = sqkm * 100
            print(f"\n{sqkm} square kilometers = {hectares:.2f} hectares")

        elif choice == "4":
            print("\nHectares → Square Kilometers")
            hectares = float(input("Enter area in hectares: "))
            sqkm = hectares / 100
            print(f"\n{hectares} hectares = {sqkm:.2f} square kilometers")

        elif choice == "5":
            print("\nAcres → Square Meters")
            acres = float(input("Enter area in acres: "))
            sqm = acres * 4046.86
            print(f"\n{acres} acres = {sqm:.2f} square meters")

        elif choice == "6":
            print("\nSquare Meters → Acres")
            sqm = float(input("Enter area in square meters: "))
            acres = sqm / 4046.86

        elif choice == "0":
           print("\nReturning to Main Menu...")
           main()

        else:
           print("\n--- ⚠️ Invalid choice, please try again. ---\n")
           continue
# ---------------------------------------------------------

# --- Volume Conversion Menu ---
def volume_conversion_menu():
    while True:
        print("\n--- Volume Conversion ---")
        print("""
           1. Liters → Milliliters
           2. Milliliters → Liters
           3. Liters → Gallons
           4. Gallons → Liters
           5. Cubic Meters → Liters
           6. Liters → Cubic Meters
           0. Back to Main Menu
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            print("\nLiters → Milliliters")
            liters = float(input("Enter volume in liters: "))
            ml = liters * 1000
            print(f"\n{liters} liters = {ml:.2f} milliliters")

        elif choice == "2":
            print("\nMilliliters → Liters")
            ml = float(input("Enter volume in milliliters: "))
            liters = ml / 1000
            print(f"\n{ml} milliliters = {liters:.2f} liters")

        elif choice == "3":
            print("\nLiters → Gallons")
            liters = float(input("Enter volume in liters: "))
            gallons = liters * 0.264172
            print(f"\n{liters} liters = {gallons:.2f} gallons")

        elif choice == "4":
            print("\nGallons → Liters")
            gallons = float(input("Enter volume in gallons: "))
            liters = gallons / 0.264172
            print(f"\n{gallons} gallons = {liters:.2f} liters")

        elif choice == "5":
            print("\nCubic Meters → Liters")
            cubic_m = float(input("Enter volume in cubic meters: "))
            liters = cubic_m * 1000
            print(f"\n{cubic_m} cubic meters = {liters:.2f} liters")

        elif choice == "6":
            print("\nLiters → Cubic Meters")
            liters = float(input("Enter volume in liters: "))
            cubic_m = liters / 1000
            print(f"\n{liters} liters = {cubic_m:.3f} cubic meters")

        elif choice == "0":
            print("\nReturning to Main Menu...")
            main()

        else:
            print("\n--- ⚠️ Invalid choice, please try again. ---\n")
            continue
# ---------------------------------------------------------

# --- Speed Conversion Menu ---
def speed_conversion_menu():
    while True:
        print("\n--- Speed Conversion ---")
        print("""
            1. Kilometers/hour → Miles/hour
            2. Miles/hour → Kilometers/hour
            3. Meters/second → Kilometers/hour
            4. Kilometers/hour → Meters/second
            5. Meters/second → Miles/hour
            6. Miles/hour → Meters/second
            0. Back to Main Menu
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            print("\nKilometers/hour → Miles/hour")
            kmh = float(input("Enter speed in km/h: "))
            mph = kmh * 0.621371
            print(f"\n{kmh} km/h = {mph:.2f} mph")

        elif choice == "2":
            print("\nMiles/hour → Kilometers/hour")
            mph = float(input("Enter speed in mph: "))
            kmh = mph / 0.621371
            print(f"\n{mph} mph = {kmh:.2f} km/h")

        elif choice == "3":
            print("\nMeters/second → Kilometers/hour")
            ms = float(input("Enter speed in m/s: "))
            kmh = ms * 3.6
            print(f"\n{ms} m/s = {kmh:.2f} km/h")

        elif choice == "4":
            print("\nKilometers/hour → Meters/second")
            kmh = float(input("Enter speed in km/h: "))
            ms = kmh / 3.6
            print(f"\n{kmh} km/h = {ms:.2f} m/s")

        elif choice == "5":
            print("\nMeters/second → Miles/hour")
            ms = float(input("Enter speed in m/s: "))
            mph = ms * 2.23694
            print(f"\n{ms} m/s = {mph:.2f} mph")

        elif choice == "6":
            print("\nMiles/hour → Meters/second")
            mph = float(input("Enter speed in mph: "))
            ms = mph / 2.23694
            print(f"\n{mph} mph = {ms:.2f} m/s")

        elif choice == "0":
            print("\nReturning to Main Menu...")
            main()

        else:
            print("\n--- ⚠️ Invalid choice, please try again. ---\n")
            continue
# ---------------------------------------------------------

# --- Energy Conversion Menu ---
def energy_conversion_menu():
    while True:
        print("\n--- Energy Conversion ---")
        print("""
            1. Joules to Calories
            2. Calories to Joules
            3. Joules to Kilowatt-hours
            4. Kilowatt-hours to Joules
            0. Back to Main Menu
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            print("\nJoules → Calories")
            joules = float(input("Enter energy in joules: "))
            calories = joules / 4.184
            print(f"\n{joules} joules = {calories:.2f} calories")

        elif choice == "2":
            print("\nCalories → Joules")
            calories = float(input("Enter energy in calories: "))
            joules = calories * 4.184
            print(f"\n{calories} calories = {joules:.2f} joules")

        elif choice == "3":
            print("\nJoules → Kilowatt-hours")
            joules = float(input("Enter energy in joules: "))
            kwh = joules / 3.6e6
            print(f"\n{joules} joules = {kwh:.6f} kWh")

        elif choice == "4":
            print("\nKilowatt-hours → Joules")
            kwh = float(input("Enter energy in kilowatt-hours: "))
            joules = kwh * 3.6e6
            print(f"\n{kwh} kWh = {joules:.2f} joules")

        elif choice == "0":
            print("\nReturning to Main Menu...")
            main()

        else:
            print("\n--- ⚠️ Invalid choice, please try again. ---\n")
            continue
# ---------------------------------------------------------

# --- Currency Conversion Menu ---
def currency_conversion_menu():
    while True:
        print("\n--- Currency Conversion ---")
        print("""
            1. USD to PKR
            2. PKR to USD
            3. EUR to PKR
            4. PKR to EUR
            0. Back to Main Menu
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            print("\nUSD → PKR")
            usd = float(input("Enter amount in USD: "))
            pkr = usd * 278.50  # Example rate
            print(f"\n{usd} USD = {pkr:.2f} PKR")

        elif choice == "2":
            print("\nPKR → USD")
            pkr = float(input("Enter amount in PKR: "))
            usd = pkr / 278.50  # Example rate
            print(f"\n{pkr} PKR = {usd:.2f} USD")

        elif choice == "3":
            print("\nEUR → PKR")
            eur = float(input("Enter amount in EUR: "))
            pkr = eur * 298.75  # Example rate
            print(f"\n{eur} EUR = {pkr:.2f} PKR")

        elif choice == "4":
            print("\nPKR → EUR")
            pkr = float(input("Enter amount in PKR: "))
            eur = pkr / 298.75  # Example rate
            print(f"\n{pkr} PKR = {eur:.2f} EUR")

        elif choice == "0":
            print("\nReturning to Main Menu...")
            main()
            
        else:
            print("\n--- ⚠️ Invalid choice, please try again. ---\n")
            continue
# ---------------------------------------------------------

# ---------- Main Function ----------
def main():
    print("\n---------- Unit Converter ----------\n")
    while True:
        print("Select Conversion Type: ")
        print("""
        1. Length
        2. Weight / Mass
        3. Temperature
        4. Time
        5. Area
        6. Volume
        7. Speed
        8. Energy
        9. Currency
        0. Exit
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            length_conversion_menu()
        elif choice == "2":
            weight_mass_conversion_menu()
        elif choice == "3":
            temperature_conversion_menu()
        elif choice == "4":
            time_conversion_menu()
        elif choice == "5":
            area_conversion_menu()
        elif choice == "6":
            volume_conversion_menu()
        elif choice == "7":
            speed_conversion_menu()
        elif choice == "8":
            energy_conversion_menu()
        elif choice == "9":
            currency_conversion_menu()
        elif choice == "0":
            print("\n--- Thanks for using Unit Converter! ---\n")
            exit()
        else:
            print("\n--- ⚠️ Invalid choice. Please enter a number between 0 and 9. ---\n")
            continue
# ---------------------------------------------------------

# ---------- Run ----------
try:
    if __name__ == "__main__":
        main()
except KeyboardInterrupt:
    print("\n--- Program Terminated! ---\n")
# ---------------------------------------------------------



