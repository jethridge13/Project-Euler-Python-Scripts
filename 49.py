# Problem: 3 4-digit prime numbers, which are separated by the same value.
# Example: "1487, 4817, 8147, in which each of the terms increases by 3330"

import functions
import time
import itertools

start = time.time()
# generate all 4 digit primes
a = 1000
b = 10000
primes = []
for i in range(a, b):
    if functions.isPrime(i):
        primes.append(i)
allPerms = []
for i in primes:
    if i % int((len(primes) / 100)) == 0:
        print(str(int((len(primes)/b)*100)) + "%")
    r = itertools.permutations(str(i))
    perms = []
    for j in r:
        number = int("".join(j))
        if number in primes:
            perms.append(number)
    if len(perms) >= 3:
        s = list(set(perms))
        if len(s) >= 3:
            allPerms.append(s)
candidates = []
for i in allPerms:
    i.sort()
    for j in i:
        for k in i:
            dif = k - j
            if dif > 0:
                c = k + dif
                if c in i:
                    l = [j, k, c]
                    candidates.append(l)
print(candidates)
functions.printTimeElapsed(start)

# Answer: The three primes are 2969, 6299, 9629. The submitted answer is 296962999629.