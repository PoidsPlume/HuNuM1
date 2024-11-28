import requests
import re
from bs4 import BeautifulSoup

#url for archives of aatds website is http://www.aatds.fr/yyyy/mm/
#link for articles is <a href='links> in h2 with class entry-title

def scrap_article_url(soup):
	list_url = []
	
	for h2 in soup.find_all("h2", attrs={"class": "entry-title"}):
		for a in h2.find_all('a', href=True):
			list_url.append(a['href'])
	print("Sucessfully scrapped all article's url from this page")
	return list_url

#def scrap_article_content(url, year, month):
#	return article_content

year = [str(y) for y in range(2020, 2025)]
month = [str(m) if len(str(m)) == 2 else '0' + str(m) for m in range(1, 13)] #add '0' before unique digits in order to have month with 2 digits

for y in year:
	for m in month:
		response = requests.get("http://www.aatds.fr/" + y + "/" + m +"/") #test all possible url
		
		if (response.status_code == 200): 
			print(f"Page {y}/{m} exists")
			soup = BeautifulSoup(response.text, "html.parser")
			list_url = scrap_article_url(soup)
			
			for url in list_url:
				scrap_article(url, y, m)
			
		
