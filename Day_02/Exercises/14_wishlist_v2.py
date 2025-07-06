import _json
import json

wishlist = [
    {
        "Name" : "Absolute",
        "Description" : "Drinking Water",
        "Size (mL)" : 1500,
        "Cost (PhP)" : 56
    },
    {
        "Name": "Coke",
        "Description": "Soda",
        "Size (mL)": 500,
        "Cost (PhP)": 35
    }
]
# Order is a dictionary in the wishlist

for order in wishlist:
    print("Item :")

    for key,value in order.items():
        print(f"\t{key}:",value)

    print()

# Save the dictionary data to a json file
with open('Grocery.json','w') as file:
    json.dump(wishlist,file,indent=1)