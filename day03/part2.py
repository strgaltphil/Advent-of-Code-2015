with open('input.txt', 'r') as file:
	data = list(file.read())
	# data = list('^>v<')

visited_houses = dict()

x, y, robo_x, robo_y = 0, 0, 0, 0

visited_houses[(x, y)] = visited_houses.get((x, y), 0) + 2

for index, direction in enumerate(data):
	if index % 2 == 1:
		if direction == '^':
			y += 1
		elif direction == '>':
			x += 1
		elif direction == 'v':
			y -= 1
		else:
			x -= 1
	else:
		if direction == '^':
			robo_y += 1
		elif direction == '>':
			robo_x += 1
		elif direction == 'v':
			robo_y -= 1
		else:
			robo_x -= 1

	visited_houses[(x, y)] = visited_houses.get((x, y), 0) + 1
	visited_houses[(robo_x, robo_y)] = visited_houses.get((robo_x, robo_y), 0) + 1

print(len([v for k, v in visited_houses.items() if v > 0]))