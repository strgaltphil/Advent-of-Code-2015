with open('input.txt', 'r') as file:
	data = list(file.read())

print(data.count('(') - data.count(')'))