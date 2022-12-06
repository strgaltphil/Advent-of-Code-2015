from functools import reduce
from operator import or_
from itertools import pairwise

with open('input.txt', 'r') as file:
	data = [line for line in file.read().split('\n')]
	data = ['ieodomkazucvgmuy']

for d in data:
	# reduce(or_, [d[index:index+2][0] == d[index:index+2][1] for index in range(1, len(d) - 1, 2)])
	# print([d[index:index+2] for index in range(1, len(d) - 1, 2)])
	# print([d[index:index+2] for index in range(0, len(d) - 1, 2)])
	for i in range(len(d)-1):
		print(d[i:i+2])

	for i in range(len(d)-2):
		l, m, r = d[i:i+3]
		print(l == r and m != r)

	print([gg for gg in [d[g:g+3] for g in range(len(d)-2)]])