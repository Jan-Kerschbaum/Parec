#File to implement the main controller function for backend operation, to be called from main.py
from app.src.related_terms import get_term_graph
from app.src.paper_seach import run_paper_search 

#Constants
SEARCH_DEPTH = 5

#Main control function for backend operation
#Return values:
#   edges: List of lists of strings, each element is a list containing the names of two nodes that share an edge
#   papers: List of lists, each element is a list containing the name, authors and id of a specific paper
def run_backend(query: str):
    # Get term graph for query
    term_graph = get_term_graph(query, SEARCH_DEPTH)
    papers = run_paper_search(term_graph, query)
    # ToDo: Construct edges from term graph
    return edges, papers
