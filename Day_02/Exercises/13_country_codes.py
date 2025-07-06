country_codes = {
    "PH": "Philippines",
    "US": "United States",
    "JP": "Japan",
    "CH": "China"
}
query = input("Enter Country Code: ")

# .get method gives result if not in the databases without error
print(country_codes.get(query,"Unknown"))

for country in country_codes:
    print(country)

for country in country_codes.values():
    print(country)

for country in country_codes.items():
    print(country,country_codes)