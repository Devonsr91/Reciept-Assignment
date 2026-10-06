item1_name = "Notebook" 
item1_price = "4.99"
item1_qty = "2"


item2_name = "Penpack"
item2_price = "7.50"
item2_qty = 1 

item3_name = "Backpack"
item3_price = "34.99"
item3_qty = "1"

tax_rate = "0.075"  # 7.5% sales tax


price1 = float(item1_price)
price2 = float(item2_price)
price3 = float(item3_price)


qty1 = int(item1_qty)
qty2 = int(item2_qty)
qty3 = int(item3_qty)

tax = float(tax_rate)


line1_total = price1 * qty1
line2_total = price2 * qty2
line3_total = price3 * qty3


Subtotal = line1_total + line2_total + line3_total

tax_amount = Subtotal  * tax

grand_total = Subtotal + tax_amount


print("=" * 40)
print("             STORE RECEIPT")
print("=" * 40)
print(f"{item1_name:<15} ${price1:.2f} x {qty1:<5} ${line1_total:.2f}")
print(f"{item2_name:<15} ${price2:.2f} x {qty2:<5} ${line2_total:.2f}")
print(f"{item3_name:<15} ${price3:.2f} x {qty3:<5} ${line3_total:.2f}")

print("=" * 40)
print(f"subtotal:                       ${Subtotal:.2f}")
print(f"tax (7.5%)                      ${tax_amount:.2f}")
print("=" * 40)
print(f"TOTAL:                          ${grand_total:.2f}")
print("=" * 40)