#!/usr/bin/env python
import sys
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

count_present = 0
count_valid = 0

for line in sys.stdin.read().split("\n\n"):
    passport = dict(l.split() for l in line.split())

    present = True
    valid = True

    for field, data in fields.items():
        if field not in passport:
            present = False
            break
        elif data.match(passport[field]) == None:
            valid = False

    count_present += present
    count_valid += present and valid

print(count_present)
print(count_valid)
