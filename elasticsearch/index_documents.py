"""Index document and load to Elasticsearch"""

import json
import requests
import sys
import pprint


data_file = './data/arxiv-metadata-oai-snapshot.json'       #load original data set

indexname = "arxiv_data_reduced"    #choose ES index name
print(indexname)

url = "http://localhost:9200/{}/_doc".format(indexname)
#cafile = 'ca.crt'
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
# username = "elastic"
# password = "admin@1234"


# see https://arxiv.org/help/api/user-manual --> only keep categories related to Computer Science

category_map = {
'cs.AI': 'Artificial Intelligence',
'cs.AR': 'Hardware Architecture',
'cs.CC': 'Computational Complexity',
'cs.CE': 'Computational Engineering, Finance, and Science',
'cs.CG': 'Computational Geometry',
'cs.CL': 'Computation and Language',
'cs.CR': 'Cryptography and Security',
'cs.CV': 'Computer Vision and Pattern Recognition',
'cs.CY': 'Computers and Society',
'cs.DB': 'Databases',
'cs.DC': 'Distributed, Parallel, and Cluster Computing',
'cs.DL': 'Digital Libraries',
'cs.DM': 'Discrete Mathematics',
'cs.DS': 'Data Structures and Algorithms',
'cs.ET': 'Emerging Technologies',
'cs.FL': 'Formal Languages and Automata Theory',
'cs.GL': 'General Literature',
'cs.GR': 'Graphics',
'cs.GT': 'Computer Science and Game Theory',
'cs.HC': 'Human-Computer Interaction',
'cs.IR': 'Information Retrieval',
'cs.IT': 'Information Theory',
'cs.LG': 'Machine Learning',
'cs.LO': 'Logic in Computer Science',
'cs.MA': 'Multiagent Systems',
'cs.MM': 'Multimedia',
'cs.MS': 'Mathematical Software',
'cs.NA': 'Numerical Analysis',
'cs.NE': 'Neural and Evolutionary Computing',
'cs.NI': 'Networking and Internet Architecture',
'cs.OH': 'Other Computer Science',
'cs.OS': 'Operating Systems',
'cs.PF': 'Performance',
'cs.PL': 'Programming Languages',
'cs.RO': 'Robotics',
'cs.SC': 'Symbolic Computation',
'cs.SD': 'Sound',
'cs.SE': 'Software Engineering',
'cs.SI': 'Social and Information Networks',
'cs.SY': 'Systems and Control'}


def get_metadata():
    with open(data_file, 'r') as f:
        for line in f:
            yield line

authors = []
titles = []
abstracts = []
years = []
categories = []
metadata = get_metadata()

for paper in metadata:
    paper_dict = json.loads(paper)
    ref = paper_dict.get('journal-ref')
    try:
        year = int(ref[-4:]) 
        if 2000 < year <= 2021:
            categories.append(category_map[paper_dict.get('categories').split(" ")[0]])
            authors.append(paper_dict.get('authors'))
            years.append(year)
            titles.append(paper_dict.get('title'))
            abstracts.append(paper_dict.get('abstract'))
    except:
        pass 

print("Check length: ", len(titles), len(abstracts), len(years), len(authors), len(categories))


reduced = []

for author, title, abstract, year, category in zip(authors, titles, abstracts, years, categories):
    reduced.append({"abstract":abstract, "title":title, "author":author, "year":year, "category":category})

data = {"root": reduced}        #add root


# index each document
count = len(data["root"])


for each in range(count):
    print(each)
    doc = data['root'][each]
    r = requests.post(url, data=json.dumps(doc), headers=headers)  #auth=(username, password), verify=cafile
    print(r.status_code)


# print number of documents in the json
print("Numbers of Docs: ", count)
print("Done!")