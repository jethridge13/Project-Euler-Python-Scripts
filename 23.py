# Problem: Find the sum of all positive integers which cannot be written as the sum of two abundant numbers
# TODO Answer is wrong and terribly inefficient
import functions
import time

start = time.time()
# Step 1: Get an array of all abundant numbers
a = 1
# Every numbe above 28123 can be written as the sum of two abundant numbers
b = 28123
allNumbers = []
abundantNumbers = []
for i in range(a, b+1):
    allNumbers.append(i)
    divisors = functions.getDivisors(i)
    if len(divisors) > 1:
        divisors.remove(max(divisors))
    if sum(divisors) > i:
        abundantNumbers.append(i)
for i in abundantNumbers:
    print(str(i))
    for j in abundantNumbers:
        n = i + j
        if n > b:
            break
        if n in allNumbers:
            allNumbers.remove(n)
print(str(allNumbers))
print(str(sum(allNumbers)))
functions.printTimeElapsed(start)