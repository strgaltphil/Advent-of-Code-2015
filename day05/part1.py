from operator import or_
from functools import reduce

with open('input.txt', 'r') as file:
	data = [line for line in file.read().split('\n')]

nice_string = 0
for d in data:
	if not reduce(or_, list(map(lambda x: x in d, ['ab', 'cd', 'pq', 'xy']))):
		if reduce(or_, [d[index:index+2][0] == d[index:index+2][1] for index in range(len(d) - 1)]):
			if sum(list(map(d.count, 'aeiou'))) >= 3:
				nice_string += 1

print(nice_string)