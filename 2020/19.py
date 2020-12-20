#!/usr/bin/env python
import sys
import re
from lark import Lark

rules, messages = sys.stdin.read().split("\n\n")
messages = messages.splitlines()


def solve(rules):
    parser = Lark(re.sub(r"(\d+)", r"t\1", rules), start="t0")
    valid = len(messages)
    for message in messages:
        try:
            parser.parse(message)
        except:
            valid -= 1
    print(valid)


solve(rules)
solve(rules
    .replace("8: 42", "8: 42 | 42 8")
    .replace("11: 42 31", "11: 42 31 | 42 11 31")
)
