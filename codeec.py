#This will not run on online IDE
import requests
from bs4 import BeautifulSoup

# URL = "https://dcecm.iitd.ac.in/skm/website/index.html"
# r = requests.get(URL)

f = open("index.html", "rb")
g = open("new.html", "w")

soup = BeautifulSoup(f.read(), 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
# print(soup.prettify())

mydivs = soup.find_all("div", {"class": "row education"})
# print(mydivs[4])

output = ""
for row in mydivs[2].findAll('p'):
    # print(row)
    output += '\n<div class="publication-item pb-0">\n'+str(row)+"\n</div>"

g.write(output)


