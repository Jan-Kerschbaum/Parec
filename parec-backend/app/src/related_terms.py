#File to implement the search for terms related to a given starting term across the search space


#Function that takes in a string and an int. Performs seach recursively up to depth times.
#To be called from controller
#Return values:
#   term_graph: Dictionary, keys = terms, values = related terms found for corresponding key
def get_term_graph(query: str, depth: int):
    ...
    return term_graph


#Function that finds terms related to source
#BERTopic call needs to go here
#Return values:
#   related_terms: List of terms found for source
def find_related_terms(source: str):
    ...
    return related_terms