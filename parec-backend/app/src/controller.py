#File to implement the main controller function for backend operation, to be called from main.py
from app.src.related_terms import get_term_graph
from app.src.paper_seach import run_paper_search
import json
import configparser

#Main control function for backend operation
#Return values:
#   edges: JSON object representing edge list of term graph
#   papers: List of lists, each element is a list containing the name, authors and id of a specific paper
def run_backend(query: str):
    '''
        Main function for backend operations

        Keyword Arguments:
            query (string): Input

        Return Values:
            edges (JSON object): Represent the edge list of the term graph
            papers (list): List of lists, each element is a list containing the name, authors, and ID of a specific paper
    '''
    config = configparser.ConfigParser()
    config.read("./hyperparameters.ini")
    search_depth = int(config["DEFAULT"]["SearchDepth"])
    words_per_search = int(config["DEFAULT"]["WordsPerSearch"])
    max_relevance = int(config["DEFAULT"]["MaxRelevance"])
    wps_decay = int(config["DEFAULT"]["WPS_Decay"])
    # Get term graph for query
    term_graph = get_term_graph(query, search_depth, words_per_search, wps_decay)
    papers = run_paper_search(term_graph, query, max_relevance)
    #Construct edges from term graph
    running_id = 0
    edges_dict = {}
    for key in term_graph.keys():
        for val in term_graph[key]:
            edges_dict[running_id] = {"from": key, "to": val}
            running_id += 1
    edges = json.dumps(edges_dict)
    return edges, papers
