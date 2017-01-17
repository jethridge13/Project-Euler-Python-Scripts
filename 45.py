import functions
import time

start = time.time()
triangle = []
pentagonal = []
hexagonal = []
a = 1
b = 100000
for i in range(a, b):
    triangle.append(functions.genTriangle(i))
    pentagonal.append(functions.genPentagonal(i))
    hexagonal.append(functions.genHexagonal(i))
print("Numbers generated.")
count = 0
for i in triangle:
    count += 1
    if count % int((len(triangle) / 100)) == 0:
        print(str(int((count/len(triangle))*100)) + "%")
    if i in pentagonal and i in hexagonal:
        print(i)
functions.printTimeElapsed(start)