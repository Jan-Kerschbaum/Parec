***
ℹ️ This directory contains the main source components of the Parec Backend Application, including the paper recommender, related term finder, and controller.
***

## `controller.py`

This module acts as a controller that handles user queries and interacts with the other modules to provide the desired output. It receives the user's query and sends the query to the appropriate modules for processing. It then formats the output for sending back to the client.

## `related_term_finder.py`

This module is responsible for finding related terms based on a user query. It uses techniques such as word embeddings and semantic similarity to identify terms that are semantically related to the query term.

Specifically, we select the n nearest embedded terms to our source term, which is initially the query. We repeat this with the newly found terms a number of times recursively, until our preset search depth is reached.

In cases where the query is not among the embedded terms, in which case our model does not support the primary method, we instead select the top words of the topic that is closes to the query, and then proceed as above.

## `paper_recommender.py`

This module provides the main functionality of the paper recommendation system. It searches through the papers and suggests the most relevant ones based on the user's input and the previously found relevant terms. The module uses various techniques such as text similarity, keyword matching, and collaborative filtering to provide accurate recommendations.

