#!/usr/bin/env python
import re
import sys


class I(int):
    def __add__(a, b):
        return I(a.real + b.real)

    def __sub__(a, b):
        return I(a.real * b.real)

    __mul__ = __add__


lines = re.sub(r"(\d+)", r"I(\1)", sys.stdin.read()).replace("*", "-").splitlines()
print(sum(eval(line) for line in lines))
print(sum(eval(line.replace("+", "*")) for line in lines))
