***
ℹ️ This directory contains the backend code of the Parec application. It includes the following subdirectories and files:
***

- **🗂️ [`app/`](parec-backend/app/data):** Contains all main code for the backend of our application.

    - **🗂️ [`data/`](parec-backend/app/data):** This directory contains various data files used for pre-processing, loading data to and from Elasticsearch, as well as pre-trained models. These files are used by the backend components to perform various tasks, such as paper recommendation and query expansion.
    
    - **🗂️ [`src/`](parec-backend/app/src):** This directory contains the main source components of the application, such as the paper recommender that searches through the papers, the code that finds related terms based on a user query and the controller that handles queries.
    
    - **🗂️ [`tests/`](parec-backend/app/tests):** This directory contains the test functions for the backend code.

- **📱 [`main.py`](parec-backend/main.py):** This file defines the FastAPI application and its routes, which specify the URL endpoints that the application can respond to and the corresponding actions it should take when those endpoints are requested.

- **⚙️ [`requirements.txt`](parec-backend/requirements.txt):** This file contains the list of dependencies required to run the backend code.

- **🛳️ [`Dockerfile`](parec-backend/Dockerfile):** This Dockerfile installs the dependencies listed in [`requirements.txt`](parec-backend/requirements.txt), copies the [`app/`](parec-backend/app/data) directory to the container, and then runs the `uvicorn` server.
