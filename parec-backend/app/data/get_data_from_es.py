from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan
import pandas as pd
import os

def get_data_from_elastic(index_name: str, save_df=False):
    """
    Retrieve data from an Elasticsearch index and return as a Pandas DataFrame.

    Args:
        index_name (str): The name of the Elasticsearch index to retrieve data from.
        save_df (bool, optional): Whether to save the DataFrame as a CSV file in a
            fixed directory. Defaults to False.
        
    Returns:
        pd.DataFrame: A Pandas DataFrame containing the retrieved data.
    """
    # Instantiate a client instance
    es = Elasticsearch("http://localhost:9200")

    # Define the Elasticsearch query to retrieve all documents in the index
    query = {
        "query": {
            "match_all": {}
        }
    }

    # Use the Elasticsearch scan API to retrieve all documents in the index
    docs = scan(client=es, query=query, index=index_name, scroll="1m")

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

    if save_df:
        directory = 'data'
        filename = 'elasticsearch_data.csv'
        if not os.path.exists(directory):
            os.makedirs(directory)
        df.to_csv(os.path.join(directory, filename), index=False)

    return df

# df = get_data_from_elastic()
# print(df.head())
