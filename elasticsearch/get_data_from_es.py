from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan
import pandas as pd

# Instantiate a client instance
es = Elasticsearch("http://localhost:9200")

# Call an API, in this example `info()`
resp = es.info()
print(resp)


def get_data_from_elastic():
    # query: The elasticsearch query.
    query = {
        "query": {
            "match": {
                "category.keyword": "Artificial Intelligence"   #insert query here
            }     
        }
    }
    # Scan function to get all the data. 
    rel = scan(client=es,             
               query=query,                                     
               scroll='1m',
               index='arxiv_data_reduced',
               raise_on_error=True,
               preserve_order=False,
               clear_scroll=True)
    # Keep response in a list.
    result = list(rel)
    temp = []
    # need only '_source', which has all the fields required.
    # elimnates the elasticsearch metadata like _id, _type, _index.
    for hit in result:
        temp.append(hit['_source'])
    #create dataframe
    df = pd.DataFrame(temp)
    return df

df = get_data_from_elastic()
print(df.head())