requests = {"Andrew": 10, "Peddy": 21, "Alex": 30}
banned = {"Alex"}

# List the adult names whose age is equal to or greater than 18
adults = [name for name,age in requests.items() if age >= 18]
print(adults)

# Deletes the banned name from the list
allowed = [name for name in adults if name not in banned]
print(allowed)