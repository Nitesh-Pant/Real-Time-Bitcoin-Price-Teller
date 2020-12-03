# Bitcoin price predictor
import requests
from bs4 import BeautifulSoup

Link = "https://www.google.com/search?q=1+bitcoin+to+inr&oq=1+bitcoin+to+inr&aqs=chrome..69i57j0i433j0l2j0i67j0l2.5316j0j4&sourceid=chrome&ie=UTF-8"
t = requests.get(Link).text
#print(t)
soup = BeautifulSoup(t, 'lxml')
#print(soup)
#print(soup.prettify())
#print(soup.title)

a = soup.find_all(class_="BNeawe iBp4i AP7Wnd")[1]
print(a.text)
