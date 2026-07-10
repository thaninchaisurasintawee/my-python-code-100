print("1. Circle Calculator:")
print("   - Ask user for radius")
print("   - Calculate area (π * r²)")
print("   - Calculate circumference (2 * π * r)")
print("   - Use 3.14159 for π")
print()
num1 = float(input("radius: "))
area = 3.14159 * num1 ** 2
circumference = 2 * 3.14159 * num1
print(f"Area : {area}")
print(f"Circumference : {circumference}")