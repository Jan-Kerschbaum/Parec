***
ℹ️ This directory contains the main source components of the Parec Backend Application, including the paper recommender, related term finder, and controller.
***

## `controller.py`

This module acts as a controller that handles user queries and interacts with the other modules to provide the desired output. It receives the user's query, determines the type of request, and sends the query to the appropriate module for processing. It then formats the output and sends it back to the client.

## `related_term_finder.py`

This module is responsible for finding related terms based on a user query. It uses techniques such as word embeddings and semantic similarity to identify terms that are semantically related to the query term.

## `paper_recommender.py`

This module provides the main functionality of the paper recommendation system. It searches through the papers and suggests the most relevant ones based on the user's input. The module uses various techniques such as text similarity, keyword matching, and collaborative filtering to provide accurate recommendations.

