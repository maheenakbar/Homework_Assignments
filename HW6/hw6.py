from bs4 import BeautifulSoup
import urllib

url = input('Please enter url to find all span tags of: ')
#use urllib to open the file to be able to read it
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
sum = 0
for tag in tags:
	 sum += int(tag.contents[0])
print (sum)