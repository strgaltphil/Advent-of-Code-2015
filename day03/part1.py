with open('input.txt', 'r') as file:
	data = list(file.read())
	# data = list('^>v<')

visited_houses = dict()

x, y = 0, 0

visited_houses[(x, y)] = visited_houses.get((x, y), 0) + 1

for direction in data:
	if direction == '^':
		y += 1
	elif direction == '>':
		x += 1
	elif direction == 'v':
		y -= 1
	else:
		x -= 1

	visited_houses[(x, y)] = visited_houses.get((x, y), 0) + 1

print(len([v for k, v in visited_houses.items() if v > 0]))