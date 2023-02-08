"""Index document and load to Elasticsearch"""

import json
import requests
import sys
import pprint


def load_to_ES(path_to_data):
    f = open(path_to_data)
    data = json.load(f)

    # index each document
    count = len(data["root"])
    indexname = "arxiv_data_reduced"    #choose ES index name
    url = "es/{}/_doc".format(indexname)    #container name "es" instead of url = "http://localhost:9200/{}/_doc".format(indexname)
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    #cafile = 'ca.crt'
    #username = "elastic"
    #password = "admin@1234"


    for each in range(count):
        #print(each)
        doc = data['root'][each]
        r = requests.post(url, data=json.dumps(doc), headers=headers)  #auth=(username, password), verify=cafile
        #print(r.status_code)

    print("Numbers of Docs: ", count)
    print("Done!")


#load_to_ES('arxiv_reduced.json')