#File to implement the search for papers based on found related terms


#Main Function to run paper search based on term graph generated in related_terms.py
#Return values:
#   papers: List of lists, each element is a list containing the name, authors and id of a specific paper
def run_paper_search(term_graph):
    ...
    return papers


#Function to construct a relevance metric from term graph
#Return values:
#   relevance_dict: Dictionary, key = term (str), value = relevance value (int) for that term
def construct_relevance_metric(term_graph):
    ...
    return relevance_dict


#Function to calculate relevance value for given paper based on precomputed relevance_list
#Return values:
#   relevance_value: Integer, representing relevance of paper according to metric
def get_paper_relevance(relevance_list, paper):
    ...
    return relevance_value
