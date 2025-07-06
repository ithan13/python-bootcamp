import json

with open('Grocery.json','r') as file:
    data = json.load(file)

print(data)