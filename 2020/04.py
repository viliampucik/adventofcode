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

present = 0
valid = 0

for line in sys.stdin.read().split("\n\n"):
    passport = dict(l.split(":") for l in line.split())

    if not passport.keys() >= fields.keys():
        continue

    present += 1
    valid += all(data.match(passport[field])
                       for field, data in fields.items())

print(present)
print(valid)
