from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan
import pandas as pd

def get_data_from_elastic():
    # Instantiate a client instance
    es = Elasticsearch("http://localhost:9200")

    # Define the Elasticsearch query to retrieve all documents in the index
    query = {
        "query": {
            "match_all": {}
        }
    }

    # Use the Elasticsearch scan API to retrieve all documents in the index
    docs = scan(client=es, query=query, index="arxiv_data_modiefied", scroll="1m")

    # Create a list of dictionaries containing only the desired fields
    data = []
    for doc in docs:
        source = doc["_source"]
        item = {
            "abstract": source.get("abstract"),
            "title": source.get("title"),
            "year": source.get("year"),
            "author": source.get("author"),
            "paper_id": source.get("paper_id"),
            "category": source.get("category")
        }
        data.append(item)

    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(data)

    return df


# def get_data_from_elastic():
#     # Instantiate a client instance
#     es = Elasticsearch("http://localhost:9200")

#     #call API
#     #resp = es.info()
#     #print(resp)

#     # query: The elasticsearch query.
#     # query = {
#     #     "query": {
#     #         "match": {
#     #             "category.keyword": "Artificial Intelligence"   #insert query here
#     #         }     
#     #     }
#     # }

#     query = {
#     "query": {
#         "match_all": {}
#         }
#     }

#     # Scan function to get all the data. 
#     rel = scan(client=es,             
#                query=query,                                     
#                scroll='1m',
#                index='arxiv_data_reduced',
#                raise_on_error=True,
#                preserve_order=False,
#                clear_scroll=True)

#     result = list(rel)
#     # need only '_source', which has all the fields required.
#     # eliminates the elasticsearch metadata like _id, _type, _index.
#     temp = []
#     for hit in result:
#         temp.append(hit['_source'])

#     #create dataframe
#     df = pd.DataFrame(temp)
#     return df

# df = get_data_from_elastic()
# print(df.head())

# df.to_csv('parec-backend/app/data/reduced_data_from_es_with_ids.csv ', index=False)