"""Index document and load to Elasticsearch"""

import sys
from typing import List, Dict
import json
import requests
from elasticsearch import Elasticsearch


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
    # open data set
    with open(path_to_data) as f:
        data = json.load(f)

    # index each document
    index_url = f"{es_url}/{index_name}/_doc"       
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    # iterate over each doc and post to ES
    count = len(data["root"]) 
    for each in range(count):
        try:
            doc = data['root'][each]
            #r = requests.post(index_url, data=json.dumps(doc), headers=headers)
            r = requests.post(index_url, data=json.dumps(doc), headers=headers, auth=("elastic","changeme"))
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Failed to index document: {doc}. {str(e)}")
        
    print("Numbers of Docs: ", count)
    print("Done!")


#load_to_ES("parec-backend/app/data/runtime/arxiv_with_stats.json", "arxiv_with_stats", "http://localhost:9200")
