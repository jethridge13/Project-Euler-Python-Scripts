# Problem: All distinct terms for a^b for 2 <= a <= 100 and 2 <= b <= 100

import functions
import time

start = time.time()
a = 2
b = 100
terms = []
for i in range(a, b+1):
    for j in range(a, b+1):
        n = i**j
        if n not in terms:
            terms.append(n)
print(len(terms))
functions.printTimeElapsed(start)

# Answer: 9183