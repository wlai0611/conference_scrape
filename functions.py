from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path
import re

def get_title_author_abstract(filename):
    '''
    Input is the filename like 2019-02-04 <Year>-<Season>-<Section>
    Output is a Pandas DataFrame that looks like this:
    title     | authors | abstract
    ---------------------------------------------
    Batteries | Walter  | Results from paper
    Potentials| Zicheng | More results from paper
    '''
    year, season, section = filename.name.replace('.html','').split('-')
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
        row.append(year)
        row.append(season)
        row.append(section)
        table.append(row)
    dataframe = pd.DataFrame(data=table,columns=['title','authors','abstract','year','season','section'])
    return dataframe

def rename_files(folder):
    html_folder = Path(folder)
    for file in html_folder.iterdir():
        old_filename = file.name
        filename_pattern = "([0-9]{4})-([0-9]{2}), Number ([0-9]{1,})"
        year, season, section = re.findall(pattern=filename_pattern, string=old_filename)[0]
        new_filename = f"{year}-{season}-{section}.html"
        file.rename( html_folder / new_filename )