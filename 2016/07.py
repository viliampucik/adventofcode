#!/usr/bin/env python
import re
import fileinput

tls_count = 0
ssl_count = 0

for line in fileinput.input():
    line = line.strip()

    tls = False
    hypernet = False
    for s in re.split(r"([^\[\]]+)", line):
        if s == "[":
            hypernet = True
        elif s == "]":
            hypernet = False
        elif len(s):
            match = re.search(r"(.)(?!\1)(.)\2\1", s)
            if match:
                if hypernet:
                    tls = False
                    break
                else:
                    tls = True
    if tls:
        tls_count += 1

    if re.search(r"""([^\[\]])(?!\1)([^\[\]])\1  # ABA
                     [^\[\]]*                    # *
                     (?:\[[^\[\]]*\][^\[\]]*)*   # optional [*]* sections
                     \[                          # [
                     [^\[\]]*                    # *
                     \2\1\2                      # BAB""", line, re.X) or \
       re.search(r"""([^\[\]])(?!\1)([^\[\]])\1  # ABA
                     [^\[\]]*                    # *
                     \]                          # ]
                     (?:[^\[\]]*\[[^\[\]]*\])*   # optional *[*] sections
                     [^\[\]]*                    # *
                     \2\1\2                      # BAB""", line, re.X):
        ssl_count += 1

print(tls_count)
print(ssl_count)
