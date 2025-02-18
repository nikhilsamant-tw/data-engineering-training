import pandas as pd
from IPython.display import display

from config.definitions import DATA_DIR, OUTPUT_DIR

df_dogs = pd.read_csv(f"{DATA_DIR}/dogs.csv")
df_cats = pd.read_csv(f"{DATA_DIR}/cats.csv")

df_dogs['kind'] = 'dog'
df_cats['kind'] = 'cat'

df_animals = pd.concat([df_dogs, df_cats], ignore_index=True)
display(df_animals)

df_animals_json = df_animals.to_json(orient='records')
display(df_animals_json)

df_animals.to_parquet(f"{OUTPUT_DIR}/animals.parquet")