item_count = int(input("Enter item count:"))
total = 0

for item in range(item_count):
    item_price = int(input("Enter item price:"))
    item_quantity = int(input("Enter item quantity:"))
    subtotal = item_price * item_quantity
    total += subtotal
    print(total)

