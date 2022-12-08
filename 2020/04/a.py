import re

with open('input.txt', 'r') as f:
    lines = f.read().split('\n\n')

required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

valid = 0
for passport in lines:
    field_count = 0
    for entry in re.split(r'\n| ', passport):
        if entry[:3] in required:
            field_count += 1
    if field_count == len(required):
        valid += 1

print(valid)
