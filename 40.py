# A number that is the product of d1, d10, d100, d1000, d100000, d100000, d10000000

import functions
import time

start = time.time()

a = 1000000
number = ""
for i in range(1, a):
    number += str(i)
one = number[1-1]
ten = number[10-1]
hundred = number[100-1]
thousand = number[1000-1]
tenThousand = number[10000-1]
hunThousand = number[100000-1]
mil = number[1000000-1]
product = int(one) * int(ten) * int(hundred) * int(thousand) * int(tenThousand) * int(hunThousand) * int(mil)
print("0." + number)
print("d_1:" + one)
print("d_10:" + ten)
print("d_100:" + hundred)
print("d_1000:" + thousand)
print("d_10000:" + tenThousand)
print("d_100000:" + hunThousand)
print("d_1000000:" + mil)
print("Product: " + str(product))

functions.printTimeElapsed(start)

"""
d_1:1
d_10:1
d_100:5
d_1000:3
d_10000:7
d_100000:2
d_1000000:1
Product: 210
Time elapsed: 2.069118022918701 seconds.
"""