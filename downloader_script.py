import sys
import requests 
from bs4 import BeautifulSoup
from datetime import date

today = date.today().strftime("%b_%d_%Y")
url = "https://bing.gifposter.com"

r = requests.get(url)
soup = BeautifulSoup(r.content,'html5lib')
imgurl = soup.find('section', attrs = {'class':'dayimg'}).img["src"][:-3]

r = requests.get(imgurl)
with open(today+".jpg", "wb") as img:
	img.write(r.content)

sys.exit()