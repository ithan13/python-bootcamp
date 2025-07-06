items = {
    "Name" : "Absolute",
    "Description" : "Drinking Water",
    "Size (mL)" : 1500,
    "Cost (PhP)" : 56
}
print("Item:")
for key , value in items.items():
    print(f"\t{key} : {value}")

items["Manufacturer"] = "AB"
print(items)