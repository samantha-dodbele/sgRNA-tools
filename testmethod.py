import pandas as pd

def test(path):

    df = pd.read_csv(path, sep='\t')
    print(df.head(0))
    print('hello')

