import pickle
import pandas as pd

df = pd.read_csv('data/title.basics.tsv.gz', sep='\t', dtype=str) # Path of the file. 
df.to_pickle("basics.pkl")
