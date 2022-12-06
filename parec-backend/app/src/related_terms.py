#File to implement the search for terms related to a given starting term across the search space
import pickle

#Constants
MODEL_FILE_PATH = ""

#Function that takes in a string and an int. Performs seach recursively up to depth times.
#To be called from controller
#Return values:
#   term_graph: Dictionary, keys = terms, values = related terms found for corresponding key
def get_term_graph(query: str, depth: int):
    term_graph = {}
    term_graph[query] = find_related_terms(query)
    for i in range(depth):
        # Flattening the list of values in the dicitonary for all keys. Each present term is a candidate for a potential search
        candidate_terms = set(sum(term_graph.values(), []))
        for term in candidate_terms:
            # No need to search for terms whose results we already have
            if not term in term_graph.keys():
                term_graph[term] = find_related_terms(term)
    # ToDo: Remove duplicate terms?
    return term_graph


#Function that finds terms related to source
#BERTopic call needs to go here
#Return values:
#   related_terms: List of terms found for source
def find_related_terms(source: str):
    # ToDo: Consider moving this out of here and passing as parameter for time impact of unpickling complex object
    file = open(MODEL_FILE_PATH, "rb")
    model = pickle.load(file)
    # Model is pickled version of BERTopic model used for clustering in preprcessing
    # ToDo: Get related terms from BERTopic model
    return related_terms