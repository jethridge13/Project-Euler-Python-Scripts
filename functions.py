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

# This function will return an array of the individual digits of a given number n
def getIndividualDigits(n):
    digits = []
    while n > 0:
        digits.append(n % 10)
        n /= 10
        n = int(math.floor(n))
    return digits[::-1]

# This function will print the elapsed time given the start time
def printTimeElapsed(start):
    end = time.time()
    print("Time elapsed: " + str(end - start) + " seconds.")