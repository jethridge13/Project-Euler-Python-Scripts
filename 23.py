# Problem: Find the sum of all positive integers which cannot be written as the sum of two abundant numbers
# TODO 
import time
import functions
import unittest

def calc():
    abundantNumbers = []
    for i in range(28124):
        if isAbundantNumber(i):
            abundantNumbers.append(i)
    
    return -1

def isAbundantNumber(n):
    divs = functions.getDivisors(n)
    del divs[-1]
    return sum(divs) > n

class Test(unittest.TestCase):

    def test1(self):
        self.assertTrue(isAbundantNumber(12))
        self.assertFalse(isAbundantNumber(28))

if __name__ == '__main__':
    start = time.time()
    unittest.main()
    print(calc())
    functions.printTimeElapse(start)