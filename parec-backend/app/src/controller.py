#File to implement the main controller function for backend operation, to be called from main.py
from app.src.related_terms import get_term_graph
from app.src.paper_seach import run_paper_search
import json

#Constants
SEARCH_DEPTH = 3 # was 5

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
    # Get term graph for query
    term_graph = get_term_graph(query, SEARCH_DEPTH)
    papers = run_paper_search(term_graph, query)
    # ToDo: Construct edges from term graph
    running_id = 0
    edges_dict = {}
    for key in term_graph.keys():
        for val in term_graph[key]:
            edges_dict[running_id] = {"from": key, "to": val}
            running_id += 1
    edges = json.dumps(edges_dict)
    return edges, papers
