string = input('Enter string: ')
special_count = 0
special_character = '!@#$%^&*()'

for character in string:
    if character in special_character:
        special_count += 1

print(special_count)