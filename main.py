from functions import get_title_author_abstract, rename_files
from pathlib import Path
import pandas as pd

files = Path("pages").iterdir()
dataframes = []
for file in files:
    dataframe = get_title_author_abstract(file)
    dataframes.append(dataframe)
big_dataframe = pd.concat(dataframes, ignore_index=True)
big_dataframe.to_csv("ecs_abstracts.csv")
print()
