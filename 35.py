# Problem: Circular primes below 1 million

import functions
import time

start = time.time()
a = 1
b = 1000000
counter = 0
primes = []
for i in range(a, b):
    if i % int((b / 100)) == 0:
        print(str(int((i/b)*100)) + "%")
    prime = True
    numbers = []
    for j in range(len(str(i))):
        word = functions.rotate(str(i), j)
        numbers.append(int(word))
    for j in numbers:
        if not functions.isPrime(j):
            prime = False
            break
    if prime:
        primes.append(i)
print("There are " + str(len(primes)) + " circular primes in the range of " + str(a) + " and " + str(b) + ".")
functions.printTimeElapsed(start)