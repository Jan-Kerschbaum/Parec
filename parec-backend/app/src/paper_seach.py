#File to implement the search for papers based on found related terms

# Constants
MAX_RELEVANCE = 10 #Placeholder, ToDo: Find good value experimentally

#Main Function to run paper search based on term graph generated in related_terms.py
#Return values:
#   papers: List of lists, each element is a list containing the name, authors and id of a specific paper
def run_paper_search(term_graph, query):
    ...
    return papers


#Function to construct a relevance metric from term graph
#Return values:
#   relevance_dict: Dictionary, key = term (str), value = relevance value (int) for that term
def construct_relevance_metric(term_graph, query):
    relevance_dict = {} # Keys are terms as strings, values are single integers representing the terms relevance rating
    relevance_dict[query] = MAX_RELEVANCE
    # Initialising, both so that each term is definitely in the dict, and so that we can track if a (non-negative) relevance has been assigned to each term  
    for term in set(sum(term_graph.values(), [])):
        relevance_dict[term] = -1
    # Iterate over the dictionary until all terms have a relevance assigned to them
    # Note that this doesn't necessarily mean that we have found the lowest possible relevance (~ shortest possible path) for lower relevances,
    # though chances are good for higher ones
    while -1 in relevance_dict.values():
        for term in relevance_dict.key():
            parent_relevances = []
            for key in term_graph.key():
                if term in term_graph[key]:
                    parent_relevances.append(relevance_dict[key])
            new_relevance = max(parent_relevances) - 1
            # We try to assign the highest possible relevance, representative of the shortest path through the graph from query to the term, to each term
            # Thus, relevances lower than the one we already have aren't relevant
            # (Realistically this probably shouldn't happen, but given the complecity of the function, this little check isn't relevant for time-complexity)
            if new_relevance > 0 and new_relevance > relevance_dict[term]:
                relevance_dict[term] = new_relevance
    return relevance_dict


#Function to calculate relevance value for given paper based on precomputed relevance_list
#Return values:
#   relevance_value: Integer, representing relevance of paper according to metric
def get_paper_relevance(relevance_list, paper):
    ...
    return relevance_value
