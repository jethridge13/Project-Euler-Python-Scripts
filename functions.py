import time
import math

# This function returns an array of all the divisors of a given number n
# It is not guaranteed to be sorted
def getDivisors(n):
    divisors = []
    limit = math.ceil(math.sqrt(n))
    for i in range(1, limit):
        if n % i == 0:
            divisors.append(i)
            if i != n/i:
                divisors.append(int(n/i))
    return divisors

# This function will return an array of the individual digits of a given number n
def getIndividualDigits(n):
    digits = []
    while n > 0:
        digits.append(n % 10)
        n /= 10
        n = int(math.floor(n))
    return digits[::-1]

# This functions transforms a given number into a Roman numeral
# It can accurately represent 1-3999 or any number if special characters (the characters with accents) are ignored.
def numberToRomanNumeral(n):
    # I = 1
    # V = 5
    # X = 10
    # L = 50
    # C = 100
    # D = 500
    # M = 1000
    numeral = ""
    thousands = n / 1000
    thousands = int(thousands)
    if thousands > 0:
        for i in range(thousands):
            numeral += "M"
    n %= 1000
    nineHundreds = n / 900
    nineHundreds = int(nineHundreds)
    if nineHundreds > 0:
        numeral += "CM"
    n %= 900
    hundreds = n / 100
    hundreds = int(hundreds)
    if hundreds > 0:
        if hundreds > 4:
            numeral += "D"
            hundreds -= 5
        if hundreds == 4:
            numeral += "CD"
        else:
            for i in range(hundreds):
                numeral += "C"
    n %= 100
    nineties = n / 90
    nineties = int(nineties)
    if nineties > 0:
        numeral += "XC"
    n %= 90
    tens = n / 10
    tens = int(tens)
    if tens > 0:
        if tens > 4:
            numeral += "L"
            tens -= 5
        if tens == 4:
            numeral += "XL"
        else:
            for i in range(tens):
                numeral += "X"
    n %= 10
    nines = n / 9
    nines = int(nines)
    if nines > 0:
        numeral += "IX"
    n %= 9
    ones = n
    if ones > 0:
        if ones > 4:
            numeral += "V"
            ones -= 5
        if ones == 4:
            numeral += "IV"
        else:
            for i in range(ones):
                numeral += "I"
    return numeral


# This function will translate from a Roman numeral to a numeric.
# It functions perfectly with numberToRomanNumeral() for all cases tested, 1-1,000,000
def numberFromRomanNumeral(n):
    # I = 1
    # V = 5
    # X = 10
    # L = 50
    # C = 100
    # D = 500
    # M = 1000
    number = 0
    n = n.upper()
    # Add a null terminator so the next character can easily be checked at the end of a string with no change in outcome
    n += "0"
    run = True
    for i in range(len(n)):
        if run:
            if n[i] == "M":
                number += 1000
            elif n[i] == "C" and n[i+1] == "M":
                number += 900
                run = False
            elif n[i] == "D":
                number += 500
            elif n[i] == "C" and n[i+1] == "D":
                number += 400
                run = False
            elif n[i] == "C":
                number += 100
            elif n[i] == "X" and n[i+1] == "C":
                number += 90
                run = False
            elif n[i] == "L":
                number += 50
            elif n[i] == "X" and n[i+1] == "L":
                number += 40
                run = False
            elif n[i] == "X":
                number += 10
            elif n[i] == "I" and n[i+1] == "X":
                number += 9
                run = False
            elif n[i] == "V":
                number += 5
            elif n[i] == "I" and n[i+1] == "V":
                number += 4
                run = False
            elif n[i] == "I":
                number += 1
        else:
            run = True
    return number



# This function will print the elapsed time given the start time
def printTimeElapsed(start):
    end = time.time()
    print("Time elapsed: " + str(end - start) + " seconds.")