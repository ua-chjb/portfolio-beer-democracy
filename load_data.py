import pandas as pd
import numpy as np

# athentication credentials using specific service account, keys downloaded locally
# import os
# from google.cloud import storage

# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "dash-app-2-happiness-and-beer-d8f67c215677.json"
# client = storage.Client()

# read in data

beer = pd.read_csv(r"https://raw.githubusercontent.com/ua-chjb/portfolio-beer-democracy/refs/heads/main/assets/data/beer_sum.csv")

dem = pd.read_csv(r"https://raw.githubusercontent.com/ua-chjb/portfolio-beer-democracy/refs/heads/main/assets/data/dem_sum.csv")

pop = pd.read_csv(r"https://raw.githubusercontent.com/ua-chjb/portfolio-beer-democracy/refs/heads/main/assets/data/pop_sum.csv")

beer = beer.rename(columns={"Unnamed: 0": "Country"})
beer = beer.set_index("Country")
beer.columns = np.arange(2008, 2019)

dem = dem.rename(columns={"Unnamed: 0": "Country"})
dem = dem.set_index("Country")
dem.columns = np.arange(2008, 2019)

pop = pop.rename(columns={"Unnamed: 0": "Country"})
pop = pop.set_index("Country")
pop.columns = np.arange(2008, 2019)

beer = beer
dem = dem
pop = pop
