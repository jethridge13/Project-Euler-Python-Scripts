# n^2 +an + b, |a| < 1000, |b| <= 1000
# Find the expression that produces the most consecutive primes

import functions
import time

def calc(a, b, n):
    return n**2 + (a*n) + b

start = time.time()

a = -999
b = -1000
max = 0
tuple = (0, 0)

while a < 1000:
    while b <= 1000:
        #print("(" + str(a) + ", " + str(b) + ")")
        prime = True
        p = []
        n = 0
        while prime:
            quadratic = calc(a, b, n)
            prime = functions.isPrime(abs(quadratic))
            if prime:
                p.append(quadratic)
            n += 1
        if len(p) > max:
            max = len(p)
            tuple = (a, b)
        b += 1
    b = 0
    a += 1

print("Max chain: " + str(max))
print(tuple)
product = tuple[0] * tuple[1]
print("The product of the coefficients is " + str(product))

functions.printTimeElapsed(start)

"""
Max chain: 71
(-61, 971)
The product of the coefficients is -59231
Time elapsed: 6.550374746322632 seconds.
"""