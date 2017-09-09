import pandas as pd
import numpy as np
import nltk
from nltk import word_tokenize
df = pd.read_csv('one_review.csv')
df['token_count'] = pd.Series(0, index=df.index)
j = len(df.index)
print df
for x in range(0, j):
    tokens = word_tokenize(df.iloc[x,3])
    df.iloc[x,9] = len(tokens)

out = df.to_json(orient='records')[1:-1].replace('},{', '} {')
with open('tokenised.json', 'w') as f:
    f.write(out)
