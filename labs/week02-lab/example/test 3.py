print("3. Compound Interest Calculator:")
print("   - Ask for principal, rate, and time")
print("   - Calculate: A = P * (1 + r/100) ** t")
print()

p = float(input("Enter principal amount: "))
r = float(input("Enter interest rate (in %): "))
t = float(input("Enter time (in years): "))

a = p * (1 + r / 100) ** t
print(f"Compound Interest: {a:.2f}")