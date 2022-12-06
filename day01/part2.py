with open('input.txt', 'r') as file:
	data = list(file.read())

floor = 0
for index, d in enumerate(data):
	if d == '(': floor += 1
	else: floor -= 1

	if floor < 0: 
		print(index + 1)
		break

