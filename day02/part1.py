from itertools import accumulate
from operator import mul

with open('input.txt', 'r') as file:
	data = [line for line in file.read().split('\n')]

def calculate():
	for d in data:

		l, w, h = map(int, d.split('x'))
		
		yield 2*l*w + 2*w*h + 2*h*l + max(accumulate(sorted(map(int, d.split('x')))[:2], mul))

print(sum(calculate()))


