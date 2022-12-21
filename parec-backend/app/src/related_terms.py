#File to implement the search for terms related to a given starting term across the search space
from top2vec import Top2Vec

#Constants
WORDS_PER_SEARCH = 5
MODEL_FILE_PATH = ""
MODEL = None

#Function that takes in a string and an int. Performs seach recursively up to depth times.
#To be called from controller
#Return values:
#   term_graph: Dictionary, keys = terms, values = related terms found for corresponding key
def get_term_graph(query: str, depth: int):
    term_graph = {}
    term_graph[query] = find_related_terms_query(query)
    for i in range(depth):
        # Flattening the list of values in the dicitonary for all keys. Each present term is a candidate for a potential search
        candidate_terms = set(sum(term_graph.values(), []))
        for term in candidate_terms:
            # No need to search for terms whose results we already have
            if not term in term_graph.keys():
                term_graph[term] = find_related_terms(term)
    # ToDo: Remove duplicate terms?
    return term_graph


def find_related_terms_query(query: str):
    load_model(False)
    related_words = []
    try:
        related_words, _ = MODEL.similar_words(keywords=[query], num_words=WORDS_PER_SEARCH, use_index=True)
    except:
        topic_words, _, _, _ = MODEL.query_topics(query=query, num_topics=1)
        #ToDo: Take topic words over several topics?
        related_words = topic_words[0][:WORDS_PER_SEARCH]
    return related_words

#Function that finds terms related to source
#BERTopic call needs to go here
#Return values:
#   related_terms: List of terms found for source
def find_related_terms(source: str):
    load_model(False)
    # Model is Top2Vec model used for clustering in preprcessing
    related_words, _ = MODEL.similar_words(keywords=[source], num_words=WORDS_PER_SEARCH, use_index=True)
    #Todo: Set ef?
    return related_words


def load_model(override: bool) -> None:
    global MODEL
    if MODEL == None or override:
        MODEL = Top2Vec.load(MODEL_FILE_PATH)
