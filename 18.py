# Find the greatest path from the top to the bottom of the triangle in '18.txt' going only to lower adjacent nodes.
import time
import functions
import unittest

def calc(data):
	data.reverse()
	for i in range(len(data)):
		if i == 0:
			continue
		for j in range(len(data[i])):
			data[i][j] += max(data[i-1][j], data[i-1][j+1])
	return data[-1][0]

def load(path):
	data = []
	with open(path, 'r') as f:
		for line in f:
			l = line.replace('\n', '').split(' ')
			l = list(map(int, l))
			data.append(l)
	return data

class Test(unittest.TestCase):

	def test1(self):
		self.assertEqual(calc(load('18Test.txt')), 23)

if __name__ == '__main__':
	start = time.time()
	#unittest.main()
	# 1074
	print(calc(load('18.txt')))
	functions.printTimeElapse(start)