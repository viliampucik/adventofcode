#!/usr/bin/env python
import fileinput
import re

fields = {
    "byr": re.compile(r"^19[23456789]\d|200[012]$"),
    "iyr": re.compile(r"^201\d|2020$"),
    "eyr": re.compile(r"^202\d|2030$"),
    "hgt": re.compile(r"^1[5678]\dcm|19[0123]cm|59in|6\din|7[0123456]in$"),
    "hcl": re.compile(r"^#[\da-f]{6}$"),
    "ecl": re.compile(r"^amb|blu|brn|gry|grn|hzl|oth$"),
    "pid": re.compile(r"^\d{9}$"),
}


def validate(passport):
    valid = True

    for field, data in fields.items():
        if field not in passport:
            return False, False
        elif data.match(passport[field]) == None:
            valid = False

    return True, valid


count_present = 0
count_valid = 0

passport = dict()
for line in fileinput.input():
    entries = dict({i[:3]: i[4:] for i in line.strip().split(" ")})
    if "" in entries:  # empty line
        (present, valid) = validate(passport)
        count_present += present
        count_valid += valid
        passport = dict()
    else:
        passport |= entries

# last line
(present, valid) = validate(passport)
count_present += present
count_valid += valid

print(count_present)
print(count_valid)
