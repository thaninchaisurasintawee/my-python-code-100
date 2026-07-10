"""
# Template 3: Shopping Calculator
shopping_calculator = '''
# Shopping Calculator Template

item_price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
discount_percent = float(input("Enter discount %: "))
tax_percent = float(input("Enter tax %: "))

# TODO: Calculate subtotal
# TODO: Calculate discount amount
# TODO: Calculate price after discount
# TODO: Calculate tax amount
# TODO: Calculate final total
# TODO: Display itemized receipt
"""

item_price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
discount_percent = float(input("Enter discount %: "))
tax_percent = float(input("Enter tax %: "))

subtotal = item_price * quantity
discount_amount = subtotal * (discount_percent / 100)
price_after_discount = subtotal - discount_amount
tax_amount = price_after_discount * (tax_percent / 100)
final_total = price_after_discount + tax_amount

print(f"Subtotal: {subtotal}")
print(f"Discount Amount: {discount_amount}")
print(f"Price After Discount: {price_after_discount}")
print(f"Tax Amount: {tax_amount}")
print(f"Final Total: {final_total}")