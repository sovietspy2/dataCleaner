import pandas as pd
from vladiate import Vlad
from vladiate.inputs import LocalFile


data = pd.read_csv("clean_data.csv", names=["sentence", "language"], delimiter=";", engine="c")
data.describe()

print(data.shape)

print(data[:10])

Vlad(source=LocalFile('clean_data.csv')).validate()