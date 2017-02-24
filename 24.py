import time
import functions
import itertools

start = time.time()
units = "0123456789"
p = itertools.permutations(units, 10)
count = 0
for i in p:
    count += 1
    if count == 1000000:
        print(i)
functions.printTimeElapsed(start)