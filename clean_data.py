# Library Imports
import pandas as pd
import numpy as np

# Loads the Dataset
df = pd.read_csv('Crime_Data_from_2020_to_Present.csv')

# Inspects the Data in the Dataset
df.head()
df.info()
df.describe()
