"""
Implements FastAPI App, which listens on port 8000 for requests from the frontend. Will need to trigger other Python components from here, ideally.
Needs to be started seperately from the frontend itself. In the finished product, this will be handeled by the docker container.

App routes:
    /
        For quick testing that the app is indeed running
    /query
        Main access point for intended functionality

"""
import os

from fastapi import FastAPI, Response, Form
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
from app.src.controller import run_backend
from .data.runtime.index_documents import load_to_ES

origins = ["http://frontend:80"]  # origin for deployment in docker

app = FastAPI()
# Adding middleware and setting allowed origins to ensure we don't get problems because both ports are on the same machine
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize ES data
try:
    load_to_ES("./app/data/runtime/arxiv_reduced_modified.json", "arxiv_data_modified", "http://es:9200")
except FileNotFoundError:
    print(f"File was not found at path {os.path.abspath(__file__)}")

class Data(BaseModel):
    query: str


def test_function(input: str):
    """
    Function to test that code on this end of the connection is executed. Returns 'works' if input is 'test', returns 'non-test input' otherwise.
    """
    if input == "test":
        return "works"
    return "non-test input"

@app.get('/health')
def health_check():
    """
    Method to serve as healthcheck.
    """

    return {"status": "ok"}

@app.post('/query')
def query_handler(query: str = Form(...)):
    """
    Method to handle POST requests from frontend for main functionality. In the body, query should contain the search term.
    """
    function_result = test_function(query)

    edges, papers = run_backend(query)

    papers_json = {}
    
    for i in range(10):
        papers_json[i] = {"name": papers[i][1], "authors": papers[i][2], "id": papers[i][0]}

    papers_json = json.dumps(papers_json)

    return Response(content=json.dumps({"result": function_result, "graph": edges, "papers": papers_json}), status_code=200)


@app.get('/')
def base_test():
    """
    Method to provide some text to the default route for testing that the app is running from the browser.
    """
    html_content = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>FastAPI middleware test</title>
        </head>
        <body>
            FastAPI entry point is running.
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
