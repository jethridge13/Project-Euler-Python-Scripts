# The sum of all amicable numbers under 10000

import time
import functions

def isAmicable(n):
    divisors = functions.getDivisors(n)
    if len(divisors) > 0:
        divisors.remove(max(divisors))
    dSum = sum(divisors)
    sumDivisors = functions.getDivisors(dSum)
    if len(sumDivisors) > 0:
        sumDivisors.remove(max(sumDivisors))
    secondSum = sum(sumDivisors)
    if secondSum == n and secondSum != dSum:
        return (n, dSum)
    return (-1, -1)

start = time.time()
amicableNumbers = []
for i in range(1, 10000):
    if i not in amicableNumbers:
        d = isAmicable(i)
        if d[0] != -1:
            if d[0] not in amicableNumbers:
                amicableNumbers.append(d[0])
            if d[1] not in amicableNumbers:
                amicableNumbers.append(d[1])
print(amicableNumbers)
print("The sum of all amicable numbers between 1 and 10,000 is " + str(sum(amicableNumbers)) + ".")
functions.printTimeElapsed(start)

# Answer: The sum of all amicable numbers between 1 and 10,000 is 31626.