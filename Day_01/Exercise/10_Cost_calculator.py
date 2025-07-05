# Ask the user for the following inputs
item_1_price = input("Input Price 1: ")
quantity_1 = input("Item 1 Qty: ")
item_2_price = input("Input Price 2: ")
quantity_2 = input("Item 2 Qty: ")
item_3_price = input("Input Price 3: ")
quantity_3 = input("Item 3 Qty: ")

# Print: Total Cost
# total = None
# print (total)

total = ((int(item_1_price)*int(quantity_1))+
         (int(item_2_price)*int(quantity_2))+
         (int(item_3_price)*int(quantity_3)))
print(total)

# subtotal_1 = int(item_1_price) * int(quantity_1)
# subtotal_2 = int(item_2_price) * int(quantity_2)
# subtotal_3 = int(item_3_price) * int(quantity_3)
# print(subtotal_1+subtotal_2+subtotal_3)