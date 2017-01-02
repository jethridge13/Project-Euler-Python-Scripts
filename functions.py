import time
import math

# This function returns an array of all the divisors of a given number n
# It is not guaranteed to be sorted
def getDivisors(n):
    divisors = []
    limit = math.ceil(math.sqrt(n))
    for i in range(1, limit):
        if n % i == 0:
            divisors.append(i)
            if i != n/i:
                divisors.append(int(n/i))
    return divisors

# This function will print the elapsed time given the start time
def printTimeElapsed(start):
    end = time.time()
    print("Time elapsed: " + str(end - start) + " seconds.")