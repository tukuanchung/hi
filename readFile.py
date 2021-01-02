# Read File

data = []
# with: close auto
with open('food.txt', 'r') as f:
	for line in f:
		data.append(line.strip())

print(data)