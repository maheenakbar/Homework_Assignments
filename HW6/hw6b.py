from bs4 import BeautifulSoup
import urllib

url = input('Enter URL: ')
count = input('Enter count: ')
count_num = int(count)
position = input('Enter position: ')
position_num = int(position)
html = urllib.request.urlopen(url).read()
list_people = list()

for num in range(count_num):
	#print (html)
	people = list()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')
	for tag in tags:
		people.append(tag.get('href', None))
	html = urllib.request.urlopen(people[position_num - 1]).read()
	list_people.append(people[position_num - 1])

print ('Retrieving:', people[0])
for item in list_people:
	print ('Retrieving:', item)



