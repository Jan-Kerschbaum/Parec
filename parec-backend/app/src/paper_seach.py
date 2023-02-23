#File to implement the search for papers based on found related terms
from app.data.get_data_from_es import get_data_from_elastic as get_dataset
from math import log as ln

# Constants
MAX_RELEVANCE = 10 #Placeholder, ToDo: Find good value experimentally

#Main Function to run paper search based on term graph generated in related_terms.py
#Return values:
#   papers: List of lists, each element is a list containing the name, authors and id of a specific paper
def run_paper_search(term_graph, query):
    '''
        Function that searches through all papers and calculates their relevance

        Keyword arguments:
            term_graph:
            query: Key term given by the user

        Return values:
            papers: List of lists, each element in the list contains a name, authors and id of a paper
    '''
    relevance_metric = construct_relevance_metric(term_graph, query)
    dataset = get_dataset()
    paper_relevances = {}
    for index, datapoint in dataset.iterrows():
        paper_relevances[datapoint["id"]] = get_paper_relevance(relevance_metric, datapoint["abstract"]) #Use ID for key?
    #Todo: Sort by values, return metadata of those papers
    papers = []
    paper_tupels = list(paper_relevances.items())
    paper_tupels.sort(key=lambda x: x[1], reverse=True)
    for i in range(10):
        p_id = paper_tupels[i][0]
        p_title = dataset.loc[dataset["id"] == p_id][0]["title"]
        p_authors = dataset.loc[dataset["id"] == p_id][0]["authors"]
        papers.append((p_id, p_title, p_authors))
    return papers


#Function to construct a relevance metric from term graph
#Return values:
#   relevance_dict: Dictionary, key = term (str), value = relevance value (int) for that term
def construct_relevance_metric(term_graph, query):
    """
        Function to construct a relevance metric from the term graph and the user input

        Keyword arguments:
            term_graph:
            query: Input of the user

        Return values:
            relevance_dict: Dictionary that contains the term and a belonging relevance value
    """
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
#   score: Integer, representing relevance of paper according to metric
def get_paper_relevance(relevance_list, paper: str):
    """
        Function that calculates the relevance for a given paper based on the precomputed relevance_list

        Keyword arguments:
            relevance_list: Precomputed list of relevances
            paper: List of lists, each element in the list consists out of a name, author and ID of a paper

        Return values:
            score: Integer, represents the relevance of a paper
    """
    # Score per word = relevance * (ln(amount of times it appears) + 1); except with 0 for 0 appearances
    # Rationale:  First appearance gives full relevance score, later appearances still benefit score but give diminishing returns
    # Especially, the discount from the nth appearance to the (n+1)th grows with n
    # So we have a big score difference between the term being mentioned 2 (~1.7 * relevance) and 5 (~2.6 * relevance), but less between 102 (~5.62 * r) and 105 (5.65 * r)
    # This seems a reasonable compromise between giving a higher score for a term being mentioned more often, and potentially overvaluing a single term 
    #
    # Consider using bases other than e for the logarithm to scale score for repeats fo the word
    score = 0
    for term in relevance_list.keys():
        # We're only counting exact matches here, we'll either have to adjust this later or preprocess papers
        appearances = paper.count(term)
        if appearances == 0:
            continue
        term_score = ln(appearances) + 1
        score += term_score * relevance_list[term]
    return score
