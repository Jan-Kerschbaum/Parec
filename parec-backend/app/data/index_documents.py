"""Index document and load to Elasticsearch"""

import sys
from typing import List, Dict
import json
import requests


def load_to_ES(path_to_data: str, index_name: str, es_url: str):
    """
    Indexes a list of JSON documents to Elasticsearch.

    Args:
        path_to_data: The path to the JSON file containing the data to be indexed.
        index_name: The name of the Elasticsearch index to use for indexing.
        es_url: The URL of the Elasticsearch cluster to use.

    Raises:
        ConnectionError: If there is a problem connecting to Elasticsearch.

    """
    with open(path_to_data) as f:
        data = json.load(f)

    # index each document
    count = len(data["root"]) 
    index_url = f"{es_url}/{index_name}/_doc"          #"http://localhost:9200/{}/_doc".format(indexname) 
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    for each in range(count):
        try:
            doc = data['root'][each]
            r = requests.post(index_url, data=json.dumps(doc), headers=headers)  #auth=(username, password), verify=cafile
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Failed to index document: {doc}. {str(e)}")
        
    print("Numbers of Docs: ", count)
    print("Done!")


#load_to_ES("parec-backend/app/data/arxiv_reduced_modified.json", "testmodified", "http://localhost:9200")