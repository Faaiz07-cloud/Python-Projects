# ---------- CSV Data Reader & Analyzer ----------

import csv # built-in module

def analyze_csv(file__path, column__name):
    values = []

    with open(file__path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row[column__name].strip():
                try:
                    values.append(float(row[column__name]))
                except ValueError:
                    pass
        if not values:
            print(f"No numeric data found in {column__name}")
    try:
        # perform basic operations
        total = sum(values)
        average = total / len(values)
        maximum = max(values)
        minimum = min(values)

        # display result
        print(f"Summary for Column: {column__name}")
        print(f"Total: {total}")
        print(f"Average: {average}")
        print(f"Maximum: {maximum}")
        print(f"Minimum: {minimum}")

    except ZeroDivisionError:
        print(f"No numeric data found in {column__name}! Please check your file path")

if __name__ == "__main__":
     file_path = "data.csv"
     column_name = "Salary"
     print("\n---------- CSV Data Reader & Analyzer ----------\n")
     analyze_csv(file_path, column_name)




