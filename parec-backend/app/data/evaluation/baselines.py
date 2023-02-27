import pandas as pd
import numpy as np
from top2vec import Top2Vec

QUERY = "Data Science"

def t2v_baseline(query: str):
    model = Top2Vec.load("../preprocessing/t2v_with_n_grams_and_args")
    abstracts = model.query_documents(query, 10)
    terms, _, _, _ = model.query_topics(query, 1)
    terms = terms[0][:20]
    return abstracts, terms.tolist()

def random_baseline(query: str):
    data = pd.read_csv(r"../preprocessing/reduced_data.csv")
    data = data.dropna()
    abstracts = data["abstract"]
    chosen_abstracts = list(abstracts.sample(10))
    all_terms = " ".join(chosen_abstracts).split(" ")
    for i in range(len(all_terms)):
        all_terms[i] = all_terms[i].lower()
    all_terms = list(set(all_terms))
    chosen_terms = np.random.choice(all_terms, 20) # Amount of terms chosen because it approximately fits with what we've seen in experiments with the system
    return chosen_abstracts, chosen_terms

random_result = random_baseline(QUERY)
t2v_result = t2v_baseline(QUERY)

print("---------------------------------------------------------------------")
print("Random abstracts:")
print(random_result[0])
print("\n")
print("Random terms:")
print(random_result[1])
print("---------------------------------------------------------------------")
print("T2V abstracts:")
print(t2v_result[0])
print("\n")
print("T2V terms:")
print(t2v_result[1])
print("---------------------------------------------------------------------")
