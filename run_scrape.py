import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


ua = UserAgent()
HEADERS = {
    'User-Agent': ua.random
}

response = requests.get("https://iopscience.iop.org/issue/2151-2043/MA2022-02/1", headers=HEADERS)
css_soup  = BeautifulSoup(response.text)
css_soup.find_all("div", class_="article-text wd-jnl-art-abstract cf")
print()