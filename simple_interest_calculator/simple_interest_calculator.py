principal = float(input("Enter the principal amount: $"))
rate = float(input("Enter the annual interest rate (%): "))
time = float(input("Enter the time in years: "))

interest = (principal * rate * time) / 100
total_amount = principal + interest

print("\nSimple Interest: $", round(interest, 2))
print("Total Amount: $", round(total_amount, 2))
