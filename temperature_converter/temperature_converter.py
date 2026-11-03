print("Temperature Converter")
print("1. Fahrenheit to Celsius")
print("2. Celsius to Fahrenheit")

choice = input("Choose 1 or 2: ")

if choice == "1":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print("Temperature in Celsius:", round(celsius, 2))

elif choice == "2":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print("Temperature in Fahrenheit:", round(fahrenheit, 2))

else:
    print("Invalid choice")
