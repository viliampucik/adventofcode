#!/usr/bin/env python
reports = [[*map(int, line.split())] for line in open(0)]


def safe(report, tolerate=0):
    for i in range(len(report) - 1):
        if not 1 <= (report[i] - report[i + 1]) <= 3:
            return tolerate and any(safe(report[j - 1 : j] + report[j + 1 :]) for j in (i, i + 1))
    return True


for tolerate in 0, 1:
    print(sum(safe(report, tolerate) or safe(report[::-1], tolerate) for report in reports))
