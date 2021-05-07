import pandas as pd
df = pd.read_csv('casas.txt',delimiter='\n')
df.to_csv('casas.csv')
