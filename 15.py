# Problem: Lattice paths. Find the number of paths from one corner to
# the other going only right and down on a 20x20 grid
# NOTE: Efficient algorithm taken from http://code.jasonbhill.com/python/project-euler-problem-15/
# My original recursive implementation was correct, but very, very slow.

import time
import functions

start = time.time()


def route_num(cube_size):
    L = [1] * cube_size
    for i in range(cube_size):
        for j in range(i):
            L[j] = L[j]+L[j-1]
        L[i] = 2 * L[i - 1]
    return L[cube_size - 1]

n = route_num(20)
print(n)
functions.printTimeElapsed(start)