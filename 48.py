# Problem: Last 10 digits of 1^1 + 2^2 + 3^3 + ... + 1000^1000
import functions
import time

def concat(s):
    if len(s) > 10:
        return s[-10:]
    return s

start = time.time()

s = 1
e = 1000
sum = 0

for i in range(s, e+1):
    power = i**i
    power = concat(str(power))
    sum += int(power)
    sum = int(concat(str(sum)))

print(sum)

functions.printTimeElapsed(start)

"""
9110846700
Time elapsed: 0.22101259231567383 seconds.
"""