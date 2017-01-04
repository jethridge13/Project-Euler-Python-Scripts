# The longest sum of consecutive primes below one million
#TODO
import functions
import time

start = time.time()
primes = []
a = 1
b = 1000000
for i in range(a, b):
    if functions.isPrime(i):
        primes.append(i)
sum = 0;
primesUsed = []
for i in primes:
    sum += i
    primesUsed.append(i)
    if sum > b:
        sum -= i
        break
found = False
while not found:
    if functions.isPrime(sum):
        found = True
    else:
        primesUsed.pop()
        sum = 0
        for i in primesUsed:
            sum += i
print("The prime " + str(sum) + " has the longest consecutive prime chain of length " + str(len(primesUsed)) + " with chain "
      + str(primesUsed))
functions.printTimeElapsed(start)