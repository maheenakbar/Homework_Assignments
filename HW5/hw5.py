import re

fhand = open('actual_data.txt')
y = list()
for line in fhand:
	line = line.rstrip()
	line_list = (re.findall('[0-9]+', line))
	if len(line_list) > 0:
		for item in line_list:
			y.append(int(item))
sum = 0
for num in y:
	sum += num

print (sum)
	