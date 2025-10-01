# ----------------- Simple Interest & EMI Calculator ---------------------

def simple_interest(principal, rate, time):
    si = (principal * rate * time) / 100
    return si

def emi(principal, annual_rate, years):
    # Convert annual rate into monthly and years into months
    monthly_rate = annual_rate / (12 * 100)
    months = years * 12

    emi_value = (principal * monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
    return emi_value


print("==== Simple Interest & EMI Calculator ====")
print("1. Calculate Simple Interest")
print("2. Calculate EMI")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    p = float(input("Enter Principal Amount: "))
    r = float(input("Enter Rate of Interest (% per year): "))
    t = float(input("Enter Time (in years): "))
    si = simple_interest(p, r, t)
    print(f"\nSimple Interest = {si}")
    print(f"Total Amount = {p + si}")

elif choice == 2:
    p = float(input("Enter Loan Amount: "))
    r = float(input("Enter Annual Interest Rate (%): "))
    t = int(input("Enter Loan Tenure (in years): "))
    emi_value = emi(p, r, t)
    print(f"\nYour Monthly EMI = {emi_value:.2f}")
    print(f"Total Payment in {t*12} months = {emi_value * t * 12:.2f}")
    print(f"Total Interest Paid = {(emi_value * t * 12) - p:.2f}")

else:
    print("Invalid Choice! Please run again.")
