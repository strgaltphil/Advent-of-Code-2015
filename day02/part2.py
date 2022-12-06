from itertools import accumulate
from operator import mul

with open('input.txt', 'r') as file:
	data = [line for line in file.read().split('\n')]

def calculate():
	for d in data:
		l = list(map(int, d.split('x')))
		
		yield sum(sorted(l)[:2]) * 2 + max(accumulate(l, mul))

print(sum(calculate()))
