
item_cost = 75.50 
tax_rate = 8.25   

tax_amount = item_cost * (tax_rate / 100)

total_cost = item_cost + tax_amount

print("Item Cost: $", item_cost)
print("Tax Rate: ", tax_rate, "%")
print("Tax Amount: $", tax_amount)
print("Total Cost: $", total_cost)