# List of item prices
prices = [50, 30, 20]        # Example prices

# List of quantities
quantities = [2, 3, 1]       # Example quantities

# Discount and Tax rates (in percentage)
discount_rate = 10           # 10% discount
tax_rate = 5                 # 5% tax

# Step 1: Calculate total amount before discount and tax
total_amount = 0
for i in range(len(prices)):
    total_amount += prices[i] * quantities[i]

# Step 2: Calculate discount amount
discount_amount = (discount_rate / 100) * total_amount

# Step 3: Subtract discount
amount_after_discount = total_amount - discount_amount

# Step 4: Calculate tax
tax_amount = (tax_rate / 100) * amount_after_discount

# Step 5: Final total cost
final_total = amount_after_discount + tax_amount

# Display results
print("Total Amount (Before Discount & Tax):", total_amount)
print("Discount Amount:", discount_amount)
print("Amount After Discount:", amount_after_discount)
print("Tax Amount:", tax_amount)
print("Final Total Cost:", final_total)
