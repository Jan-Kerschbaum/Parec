# 💡 Parec

Parec is a web application that offers a comprehensive solution for knowledge discovery and research recommendations. By taking in a user query on a particular topic, it quickly generates a knowledge graph of related concepts and recommends the top cientific articles from the [arXiv](https://arxiv.org/) database to match the user's interests. Parec streamlines the process of finding relevant information and provides an innovative solution for researchers and students alike.

The application consists of a backend and a frontend. The backend is responsible for retrieving data from [Elasticsearch](https://www.elastic.co/de/) and providing it to the frontend via a REST API. The frontend is a web application that allows users to search and view recommended articles.

***
## Team Members
- Jan Kerschbaum; ✉️ [jankerschbaum@web.de](mailto:jankerschbaum@web.de)
- Sandra Friebolin; ✉️ [sandra_friebolin@web.de](mailto:sandra_friebolin@web.de)
- Dilara Aykurt; ✉️ [d.aykurt@web.de](mailto:d.aykurt@web.de)
- Annalena Frey; ✉️ [pf225@stud.uni-heidelberg.de](mailto:pf225@stud.uni-heidelberg.de)

***
## Table of contents
1. 🛠️ [Set Up](#set-up)
2. ⚙️  [Usage](#usage)
3. 🏯 [Code Structure](#code-structure)
    1. [Backend](#backtranslation)
    2. [Frontend](#mixup)
4. 🗃️ [Data](#data)
5. 📑 [References](#references)

***
## 🛠️ Set Up <a name="setup"></a>

### Prerequisites

To run Parec, you need to have Docker and Docker Compose installed on your system.

### Running the Application

1. Clone the repository: `git clone https://github.com/Jan-Kerschbaum/Parec.git`
2. Navigate into the Parec directory: `cd Parec`
3. Run the following command to start the application: `docker-compose build` ➡️ `docker-compose up`
4. Open a web browser and go to http://localhost:9200. The frontend should now be running.

***
## ⚙️ Usage <a name="usage"></a>

1. Use the search bar to search for topics you are interested in. ℹ️ Note that the current version is restricted to topics related to computer science.
2. Click on a link to view the paper on [arXiv](https://arxiv.org/).

***
## 🏯 Code-Structure <a name="code-structure"></a>

### Backend

The main functionality of the backend is to handle the incoming user queries, retrieve data from Elasticsearch and provide it to the frontend in the desired format. The backend is written in Python and uses the [Flask](https://flask.palletsprojects.com/en/2.2.x/) web framework and Elasticsearch. It provides a REST API for the frontend to interact with. 

The code is organized into the following directories:

- `app`: This directory contains the main Flask application code, including the endpoints that handle incoming requests and return the relevant responses.

- `data`: This directory contains the scripts that are responsible for loading the data from Elasticsearch, transforming it as necessary, and returning it to the application.

- `models`: This directory contains the definition of the models used by the backend, including the Elasticsearch mappings used to index the data.


### Frontend

The Parec frontend is a web-based user interface for the Parec application. It allows users to input a query and receive a list of recommended research papers based on the query, as well as a visual representation of the relationships between topics related to the query. It is built using the [React](https://reactjs.org/) framework, with additional libraries for data visualization. It communicates with the backend using HTTP requests to receive search results and topic data.

The Parec frontend code is organized into several directories and files:

- `public/`: This directory contains the public assets for the frontend, such as the index.html file and the favicon.

- `src/`: This directory contains the source code for the frontend.

- `App.js`: The main entry point for the frontend, which contains the UI elements for the query input and search results.

- `Graph.js`: The component responsible for rendering the topic graph visualization using D3.js.

- `Search.js`: The component responsible for rendering the search results list and handling search requests.

- `utils.js`: Helper functions used throughout the frontend code.

- `package.json`: Contains metadata about the frontend, such as dependencies and scripts for building and running the application.