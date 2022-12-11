# Parec
This project is part of the _Data Science for Text Analytics_ class of Heidelberg University. Its aim is the creation a tool which recommends different scientific papers based on an input term by the user. 


### Team Members
- Jan Kerschbaum; jankerschbaum@web.de
- Sandra Friebolin; sandra_friebolin@web.de
- Dilara Aykurt; d.aykurt@web.de
- Annalena Frey; pf225@stud.uni-heidelberg.de

### Existing Code Fragment

Aside from the libraries indicated below, the project employs a pre-trained BERTopic model, as well as Svelte and one of its provided templates for the implementation of the frontend. No further pre-existing code is employed at this time.

### Utilized libraries

#### Frontend

The frontend depends on the JQuery and Vis packages. Additionally, Svelte, Vite, and the Svelte Vite plugin are required dev dependencies. 

#### Backend

The current implementation of the backend on the main branch employs the FastApi, Pydantic, Uvicorn and Python-Multipart modules.

Certain branches, especially those where work is done on implementing the backend may have additional dependencies, as indicated by the requirements.txt file on the respective branch.

### Contributions
Jan Kerschbaum mainly focused on the implementation of the frontend 
Dilara Auykurth set up a Docker for the project.
Annalena Frey and Sandra Friebolin are working with the Dataset, currently figuring out how to preprocess the dataset before using BERt

## Project State

### Planning State
Docker containers have been set up.

The frontend is largely finished, though it may be reworked should issues arise in practical operation.

The implementation of the backend has begun on other branches, but is in a partial stage. A structure for the backend has been established, and certain helper functions implemented, on other branches.

In terms of the dataset, test runs have been executed with the dataset without any preprocessing. The results clearly indicate that the data needs to be preprocessed, as the currently identified topics are full of stop words.

### Future Planning

Immediate priorities include the implementation of the function to find terms related to a source term, which itself requires us to get the functionality to get the model (after fitting to the dataset) saved and later loaded in the same state running. Additionally, the implementation of helper functions to retieve the data from ElasticSearch and make it useable in the backend is a high priority, as is the implementation of the ElasticSearch container itself.

We are currently planning to finish working with the dataset and creating a usable model by the end of december.
The backend should be finished by mid/end of january.
In mid february, we are planning to finish the implementation, so that we can create the video presentation between mid and end of february.
The report should be finished by begin of march.

### High-level Architecture Description

First, we filter stop words from and apply a lemmatizer to the abstracts of the papers in our data. This is still a work in process.

Before runtime, the papers in the dataset are clustered using BERTopics topic modeling function in order to limit the search space later on.

At runtime, a typical query is handeled as follows: It is sent from the frontend to the backend without alteration once the user presses the search button. There, we perform a search to find terms that are, in an abstract sense, related to the query, from those present in our dataset. We perfomr this search recursively, effectively creating a graph where the terms are nodes, and the relation of which terms search (first) found which other term defines edges (though despite implications, we do not use directional edges). We then construct a relevance metric on this graph, assigning to each term a relevance that declines as we move outwards from the node representing the user query. Finally, we get potentially relevant candidate papers from our reduced search space, and rank them on the basis of our relevance metric. The top candidate papers, together with their metadata (titles, authors, ARXIV IDs) are sent to the frontend, along with the graph defined through its list of edges, and visualised there.

Major deviations include if the user sends an empty query (in which case we clear both the graph and the list and show an error message), if the backend is not initialised or unreachable due to some error (error message only), or the initial state of the application prior to any query being sent, which uses example data.

### Experiments
As mentioned before, test runs with BERTtopic have been executed without preprocessed data.
As a result, we got the following topics:

|   | Topic | Count | Name |
----|-------|------|-----  |
| 0 | -1    | 7644  | -1_the_of_and_to |
| 1 | 0     | 1920  | 0_the_of_and_channel |
| 2 | 1     |882    | 1_security_the_and_of |
| 3 | 2     |828    | 2_of_the_we_is |
| 4 | 3     |667    | 3_software_of_and-to |
| 5 | 4     |640    | 4_the_neural_of_deep |
| 6 | 5     |601    | 5_language_word_translation_the |
| 7 | 6     |402    | 6_robot_robots_the_control |
| 8 | 7     |348    | 7_social_media_of_news |
| 9 | 8     |308    | 8_workshop_volume_processings_international |

## Data Analysis
### Data Sources
The dataset that we use is provided by https://www.kaggle.com/datasets/Cornell-University/arxiv?resource=download 

### Preprocessing

The extent of our preprocessing is limited, since we rely in large part on the intrinsic structure of the abstracts in our dataset. We filter out stop words and lemmatize the abstracts in our dataset to enhance the quality of the result both when clustering the abstracts and when searching for related terms. We do not apply further preprocessing of the text, in order to keep the subtextual relations between the words intact, as well as because we employ a BERTopic model at several points, which, to some extent, implements its own preprocessing.

### Basic Statistics

During experimenting with the dataset, we included all papers which were published between 2011 and 2021, which resulted in 18015 papers

### Example

Example is taken as-is from data source (https://www.kaggle.com/datasets/Cornell-University/arxiv?resource=download), though we only use certain keys (id, authors, title and abstract), allowing us to de facto reduce the dataset to the data for those keys. Each datapoint is available as a JSON object in the following format.
Unfortunaltely, due to the size of the dataset, we can not have a look at it directly, as when opening in it throws an error stating that it needs more memory to be opened.

"root":{
    "id":"0704.0001"
    "submitter":"Pavel Nadolsky"
    "authors":"C. Bal\'azs, E. L. Berger, P. M. Nadolsky, C.-P. Yuan"
    "title":"Calculation of prompt diphoton production cross sections at Tevatron and LHC energies"
    "comments":"37 pages, 15 figures; published version"
    "journal-ref":"Phys.Rev.D76:013009,2007"
    "doi":"10.1103/PhysRevD.76.013009"
    "report-no":"ANL-HEP-PR-07-12"
    "categories":"hep-ph"
    "license":NULL
    "abstract":" A fully differential calculation in perturbative quantum chromodynamics is presented for the production of massive photon pairs at hadron colliders. All next-to-leading order perturbative contributions from quark-antiquark, gluon-(anti)quark, and gluon-gluon subprocesses are included, as well as all-orders resummation of initial-state gluon radiation valid at next-to-next-to-leading logarithmic accuracy. The region of phase space is specified in which the calculation is most reliable. Good agreement is demonstrated with data from the Fermilab Tevatron, and predictions are made for more detailed tests with CDF and DO data. Predictions are shown for distributions of diphoton pairs produced at the energy of the Large Hadron Collider (LHC). Distributions of the diphoton pairs from the decay of a Higgs boson are contrasted with those produced from QCD processes at the LHC, showing that enhanced sensitivity to the signal can be obtained with judicious selection of events. "
    "versions":[
        0:{
            "version":string"v1"
            "created":string"Mon, 2 Apr 2007 19:18:42 GMT"
        }
        1:{
            "version":string"v2"
            "created":string"Tue, 24 Jul 2007 20:10:27 GMT"
        }
    ]
    "update_date":"2008-11-26"
    "authors_parsed":[
        0:[
            0:"Balázs"
            1:"C."
            2:""
        ]
        1:[
            0:"Berger"
            1:"E. L."
            2:""
        ]
        2:[
            0:"Nadolsky"
            1:"P. M."
            2:""
        ]
        3:[
            0:"Yuan"
            1:"C. -P."
            2:""
        ]
    ]
}
