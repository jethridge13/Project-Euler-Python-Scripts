import time
import functions
import math

def generateSquareDigitChain(n):
    chain = [n]
    run = True
    while run:
        d = chain[-1]
        digits = functions.getIndividualDigits(d)
        dSum = 0
        for i in digits:
            dSum += i**2
        if dSum == 89 or dSum == 1:
            chain.append(dSum)
            run = False
        else:
            chain.append(dSum)
    return chain

start = time.time()
endsIn89 = 0
a = 1
b = 10000000
for i in range(a, b):
    if i % int((b / 100)) == 0:
        print(str(int((i/b)*100)) + "%")
    chain = generateSquareDigitChain(i)
    if chain[-1] == 89:
        endsIn89 += 1
print("There are " + str(endsIn89) + " square digit chains that end in 89 between one and ten million.")
functions.printTimeElapsed(start)

# Answer: There are 8581146 square digit chains that end in 89 between one and ten million.