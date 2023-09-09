from bs4 import BeautifulSoup
import pandas as pd

filename="1.html"

def get_title_author_abstract(filename):
    '''
    Input is the filename like 2019-02-04 <Year>-<Season>-<Section>
    Output is a Pandas DataFrame that looks like this:
    title     | authors | abstract
    ---------------------------------------------
    Batteries | Walter  | Results from paper
    Potentials| Zicheng | More results from paper
    '''
    html_text = open(filename,"r",encoding='utf-8').read()
    soup = BeautifulSoup(html_text, 'html.parser')
    abstract_list = soup.find_all(attrs={"itemprop": "description"})
    title_list = soup.find_all(attrs={"class":"art-list-item-title"})
    authors_list = soup.find_all(attrs={"class":"art-list-item-meta"})
    table = []
    for title, author, abstract in zip(title_list, authors_list, abstract_list):
        row = []
        row.append(title.text)
        row.append(author.text)
        row.append(abstract.text)
        table.append(row)
    dataframe = pd.DataFrame(data=table,columns=['title','authors','abstract'])
    return dataframe
