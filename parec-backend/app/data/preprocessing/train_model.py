from top2vec import Top2Vec
import pandas as pd

df = pd.read_csv("reduced_data_from_es.csv")
df = df["abstract"]
df_list = list(df) # list of abstracts represented as strings
t2v = Top2Vec(df_list)
t2v.save("t2v_model")