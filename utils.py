from weightedGrapgh import WeightedGraph
import pandas as pd

df = pd.read_csv('critical_path/TOY.csv', ",")
print(df["Nome"].unique()[1])


