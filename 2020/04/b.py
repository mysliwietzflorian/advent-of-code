import re

with open('input.txt', 'r') as f:
    lines = f.read().split('\n\n')

required = {
    'byr': r'byr:(19[2-9]\d|200[0-2])\b',
    'iyr': r'iyr:(201\d|2020)\b',
    'eyr': r'eyr:(202\d|2030)\b',
    'hgt': r'hgt:((1[5-8]\d|19[0-3])cm|(59|6\d|7[0-6])in)\b',
    'hcl': r'hcl:(#[0-9a-f]{6})\b',
    'ecl': r'ecl:(amb|blu|brn|gry|grn|hzl|oth)\b',
    'pid': r'pid:(\d{9})\b',
}

valid = 0
for passport in lines:
    field_count = 0
    for entry in re.split(r'\n| ', passport):
        if entry[:3] in required and re.search(required[entry[:3]], entry):
            field_count += 1

    if field_count == len(required):
        valid += 1

print(valid)
