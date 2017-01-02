# Problem: What is the first triangle number to have over 500 divisors?

import math
import time
import functions

def getTriangleNumber(n):
    a = 0
    for i in range(n + 1):
        a += i
    return a

def iterateThroughTriangleNumbers(start, divisors, verbose):
    if verbose:
        print("Finding the first triangle number to have over " + str(divisors) + " divisors starting at " + str(start))
    found = False
    n = start
    t = 0
    d = 0
    while not found:
        t = getTriangleNumber(n)
        n += 1
        d = functions.getDivisors(t)
        if verbose:
            print(str(t) + ": " + str(len(d)))
        if len(d) > divisors:
            found = True
    if verbose:
        print("Found " + str(t) + " with " + str(len(d)) + " divisors.")
    return t

start = time.time()
t = iterateThroughTriangleNumbers(1, 500, True)
print(str(t))
end = time.time()
print("Time elapsed: " + str(end - start) + " seconds.")

#Answer: Found 76576500 with 576 divisors.