# Parec

### Team Members
- Jan Kerschbaum; jankerschbaum@web.de
- Sandra Friebolin; sandra_friebolin@web.de
- Dilara Aykurt; d.aykurt@web.de
- Annalena Frey; pf225@stud.uni-heidelberg.de

### Existing Code Fragment

Aside from the libraries indicated below, the project employs a pre-trained BERTopic model, as well as Svelte and one of its provided templates for the implementation of the froentd. No further pre-existing code is employed at this time.

### Utilized libraries

#### Frontend

The frontend depends on the JQuery and Vis packages. Additionally, Svelte, Vite, and the Svelte Vite plugin are required dev dependencies. 

#### Backend

The current implementation of the backend on the main branch employs the FastApi, Pydantic, Uvicorn and Python-Multipart modules.

Certain branches, especially those where work is done on implementing the backend may have additional dependencies, as indicated by the requirements.txt file on the respective branch.

### Contributions

TODO

## Project State

### Planning State

The frontend is largely finished, though it may be reworked should issues arise in practical operation.

The implementation of the backend has begun on other branches, but is in a partial stage. A structure for the backend has been established, and certain helper functions implemented, on other branches.

### Future Planning

Immediate priorities include the implementation of the function to find terms related to a source term, which itself requires us to get the functionality to get the model (after fitting to the dataset) saved and later loaded in the same state running. Additionally, the implementation of helper functions to retieve the data from ElasticSearch and make it useable in the backend is a high priority, as is the implementation of the ElasticSearch container itself.

### Architecture Description

(Preprocessing?)

Before runtime, the papers in the dataset are clustered using BERTopics topic modeling function in order to limit the search space later on.

At runtime, a typical query is handeled as follows: It is sent from the frontend to the backend without alteration once the user presses the search button. There, we perform a search to find terms that are, in an abstract sense, related to the query, from those present in our dataset. We perfomr this search recursively, effectively creating a graph where the terms are nodes, and the relation of which terms search (first) found which other term defines edges (though despite implications, we do not use directional edges). We then construct a relevance metric on this graph, assigning to each term a relevance that declines as we move outwards from the node representing the user query. Finally, we get potentially relevant candidate papers from our reduced search space, and rank them on the basis of our relevance metric. The top candidate papers, together with their metadata (titles, authors, ARXIV IDs) are sent to the frontend, along with the graph defined through its list of edges, and visualised there.

Major deviations include if the user sends an empty query (in which case we clear both the graph and the list and show an error message), if the backend is not initialised or unreachable due to some error (error message only), or the initial state of the application prior to any query being sent, which uses example data.

## Data Analysis

### Preprocessing

(Preprocessing)

### Statistics

(Statistics)

### Example


