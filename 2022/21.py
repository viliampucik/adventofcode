#!/usr/bin/env python
def solve(e):
    actions = m[e]
    if len(actions) == 1:
        return actions[0]

    a, op, b = actions
    return "(" + solve(a) + op + solve(b) + ")"


m = {
    monkey: actions.split(" ")
    for line in open(0).read().splitlines()
    for monkey, actions in [line.split(": ")]
}

print(int(eval(solve("root"))))

# Kudos to https://www.reddit.com/r/adventofcode/comments/zrav4h/comment/j133ko6/
m["humn"], m["root"][1] = ["-1j"], "-("
c = eval(solve("root") + ")")
print(int(c.real / c.imag))

# # Using z3 solver
#
# import z3
#
# m["humn"], m["root"][1] = ["humn"], "=="
#
# humn = z3.Int("humn")
# s = z3.Solver()
# s.add(eval(solve("root")))
# s.check()
# print(s.model()[humn])
