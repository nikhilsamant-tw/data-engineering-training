import pandas as pd
from IPython.display import display

from config.definitions import DATA_DIR

df_dogs = pd.read_csv(f"{DATA_DIR}/dogs.csv")
df_cats = pd.read_csv(f"{DATA_DIR}/cats.csv")

df_animals = pd.concat([df_dogs, df_cats], ignore_index=True)
display(df_animals)

df_animals_json = df_animals.to_json(orient='records')
display(df_animals_json)

df_animals.to_parquet(f"{DATA_DIR}/animals.parquet")