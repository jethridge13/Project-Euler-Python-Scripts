# Count the number of letters

from num2words import num2words
import re
import time

def returnNumbersOnly(string):
    return re.sub('[^09a-zA-Z]+', '', string)

def rangeForNumbers(start, end):
    sum = 0
    for i in range(start, end + 1):
        sum += len(returnNumbersOnly(num2words(i)))
    return sum

start = time.time()
s = 1
e = 1000
sum = rangeForNumbers(s, e)
print("The sum of the letters of the words from " + str(s) + " to " + str(e) + " is " + str(sum))
end = time.time()
print("Time elapsed: " + str(end - start) + " seconds.")

# Answer: The sum of the letters of the words from 1 to 1000 is 21124