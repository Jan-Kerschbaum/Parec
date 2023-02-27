#File to implement the search for terms related to a given starting term across the search space
from top2vec import Top2Vec
import nltk
from nltk.corpus import stopwords

#Constants
WORDS_PER_SEARCH = 3 # was 5
MODEL_FILE_PATH = r"./app/data/t2v_with_n_grams_and_args"
MODEL = None

#Function that takes in a string and an int. Performs seach recursively up to depth times.
#To be called from controller
#Return values:
#   term_graph: Dictionary, keys = terms, values = related terms found for corresponding key
def get_term_graph(query: str, depth: int):
    '''
        Function that builds the term graph. It searches recursively up to depth times.

        Keywords Arguments:
            query (string) : Input by the user
            depth (int): Number of execution times of the related-term-search

        Return Values:
            term_graph (dict): Dictionary; keys = terms, values = related terms found for the corresponding key

    '''
    term_graph = {}
    term_graph[query] = find_related_terms_query(query)
    for i in range(depth):
        # Flattening the list of values in the dicitonary for all keys. Each present term is a candidate for a potential search
        #candidate_terms = set(sum(term_graph.values(), []))
        candidate_terms = list(term_graph.values())
        candidate_terms = [item for sublist in candidate_terms for item in sublist]
        for term in candidate_terms:
            # No need to search for terms whose results we already have
            if not term in term_graph.keys():
                term_graph[term] = find_related_terms(term)
    # ToDo: Remove duplicate terms?
    return term_graph


def find_related_terms_query(query: str):
    '''
        Function for finding related terms for a given query

        Keyword Arguments:
            query (string): Input

        Return Values:
            related_words (list): List of related terms found for query
    '''
    load_model(False)
    related_words = []
    try:
        related_words, _ = MODEL.similar_words(keywords=[query], num_words=WORDS_PER_SEARCH)
    except:
        topic_words, _, _, _ = MODEL.query_topics(query=query, num_topics=1)
        related_words = topic_words[0][:WORDS_PER_SEARCH]
    return related_words

    # load_model(False)
    # related_topics = []
    # try:
    #     related_topics, _, _, _ = MODEL.search_topics(keywords=[query], num_topics=WORDS_PER_SEARCH)
    # except:
    #     topic_words, _, _, _ = MODEL.search_topics(keywords=[query], num_topics=1)
    #     related_topics = topic_words[0][:WORDS_PER_SEARCH]
    # #related_topics = [topic for topic in related_topics if topic.lower() not in stop_words]
    # return related_topics



#Function that finds terms related to source
#Return values:
#   related_terms: List of terms found for source
def find_related_terms(source: str):
    '''
        Function for finding related terms with a Top2Vec model

        Keyword Arguments:
            source (string): Input

        Return Values:
            related_words (list): List of terms found for source

    '''
    load_model(False)
    # Model is Top2Vec model used for clustering in preprocessing
    related_words, _ = MODEL.similar_words(keywords=[source], num_words=WORDS_PER_SEARCH)
    return related_words

    # load_model(False)
    # # Model is Top2Vec model used for clustering in preprocessing    
    # related_topics, _, _, _ = MODEL.search_topics(keywords=[source], num_topics=WORDS_PER_SEARCH)
    # return related_topics



def load_model(override: bool) -> None:
    '''
        Function for loading the Top2Vec model

        Keyword Arguments:
            override (bool):

        Return Values:
            none
    '''
    global MODEL
    if MODEL == None or override:
        MODEL = Top2Vec.load(MODEL_FILE_PATH)

    # global MODEL
    # if MODEL is None or override:
    #     stop_words = set(stopwords.words('english'))
    #     MODEL = Top2Vec.load(MODEL_FILE_PATH, stop_words=stop_words)
