"""
BMI Calculator (20 points)

Write a program that:

Asks for weight in kilograms
Asks for height in meters
Calculates BMI using formula: BMI = weight / (height²)
Displays BMI with 1 decimal place
Shows BMI category based on the ranges below

BMI Categories:

Below 18.5: Underweight
18.5 - 24.9: Normal weight
25.0 - 29.9: Overweight
30.0 and above: Obese

"""
weight = float(input("Weight: "))
height = float(input("Height: "))

bmi = weight / (height * height)

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"BMI = {bmi:.1f}")
print("Category =", category)

"""
Question 2: Currency Converter (20 points)

Write a program that converts between Thai Baht (THB) and US Dollars (USD).
Requirements:

Ask user to choose conversion direction (THB to USD or USD to THB)
Ask for the amount to convert
Use exchange rate: 1 USD = 35.5 THB
Display result with 2 decimal places
Show the calculation formula used
"""

exchange_rate = 35.5

print("1. THB to USD")
print("2. USD to THB")

choice = input("Choose conversion direction (1 or 2): ")
amount = float(input("Enter the amount: "))

if choice == "1":
    result = amount / exchange_rate

    print("Formula: THB / 35.5 = USD")
    print(format(amount, ".2f"), "THB =", format(result, ".2f"), "USD")

elif choice == "2":
    result = amount * exchange_rate

    print("Formula: USD * 35.5 = THB")
    print(format(amount, ".2f"), "USD =", format(result, ".2f"), "THB")

else:
    print("Invalid choice")