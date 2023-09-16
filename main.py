from functions import get_title_author_abstract, rename_files
from pathlib import Path
import pandas as pd
import re

folder_with_html = "data\ECS_abstract_html-20230916T192445Z-002\ECS_abstract_html"
rename_files(folder_with_html)
files = Path(folder_with_html).iterdir()

dataframes = []
for file in files:
    if file.is_file() and re.findall('([0-9]+)-([0-9]+)-([0-9]+)',file.name):
        dataframe = get_title_author_abstract(file)
        dataframes.append(dataframe)
big_dataframe = pd.concat(dataframes, ignore_index=True)
big_dataframe.to_csv("ecs_abstracts.csv")
print()
