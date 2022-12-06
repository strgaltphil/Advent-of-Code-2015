import hashlib

with open('input.txt', 'r') as file:
	data = file.read()

def number_generator():
	i = 0
	while True:
		yield i
		i +=1

for i in number_generator():
	if hashlib.md5(f"{data}{i}".encode()).hexdigest()[:6] == '000000':
		print(i)
		break
