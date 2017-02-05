import time
import functions

start = time.time()
n = 1
found = False
while not found:
    s = functions.genFibonacci(n)
    sStr = str(s)
    sLen = len(sStr)
    if sLen == 1000:
        found = True
    else:
        n += 1
print("Sequence number: " + str(n))
print("Digit: " + str(s))
functions.printTimeElapsed(start)