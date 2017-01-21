# Problem: Find the total score of all the names in a given file. Score goes as follows:
# A name is given a score based on the letters. A = 1, B = 2, etc.
# That score is multiplied by its position in the list.
import functions
import time

# This funciton takes a string, which is a name, and returns it's associated score.
def getNameScore(n):
    score = 0
    for i in n:
        l = ord(i)
        if l > 64 and l < 91:
            score += l - 64
    return score

start = time.time()
f = open("22.txt", "r")
line = f.read()
f.close()
names = line.split(",")
names.sort()
count = 1
totalScore = 0
for i in names:
    score = getNameScore(i)
    posScore = count * score
    totalScore += posScore
    count += 1
print(totalScore)
functions.printTimeElapsed(start)

# Answer: 871198282