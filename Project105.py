import csv
import pandas as pd
import numpy as np

data = pd.read_csv('data.csv')
print(data)
o = np.std(data)
print(o)