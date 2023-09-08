from bs4 import BeautifulSoup

filename="1.html"
html_text = open(filename,"r",encoding='utf-8').read()

soup = BeautifulSoup(html_text, 'html.parser')
paragraph_list = soup.find_all(attrs={"itemprop": "description"})
