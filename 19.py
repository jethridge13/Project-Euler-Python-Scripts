# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

import functions
import time
import datetime

start = time.time()

sundays = 0
for i in range(1901, 2001):
    for j in range(1, 13):
        if datetime.date(i, j, 1).weekday() == 6:
            sundays += 1
print(sundays)

functions.printTimeElapsed(start)

"""
171
Time elapsed: 0.0010001659393310547 seconds.
"""
