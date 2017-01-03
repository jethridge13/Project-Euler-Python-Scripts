# Problem: Take the 89.txt file and see if it can be improved, counting the total number of characters saved.

import functions
import time

start = time.time()
chars = 0
f = open("89.txt", "r")
for line in f:
    l = line[:len(line)-1]
    number = functions.numberFromRomanNumeral((l))
    improved = functions.numberToRomanNumeral(number)
    if len(str(l)) > len(improved):
        chars += len(l) - len(improved)
print("File can be improved by " + str(chars) + " characters.")
functions.printTimeElapsed(start)
