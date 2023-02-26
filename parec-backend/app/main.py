"""
Implements FastAPI App, which listens on port 8000 for requests from the frontend. Will need to trigger other Python components from here, ideally.
Needs to be started seperately from the frontend itself. In the finished product, this will be handeled by the docker container.

App routes:
    /
        For quick testing that the app is indeed running
    /query
        Main access point for intended functionality

Required packages: fastapi, python-multipart
"""
import os

from fastapi import FastAPI, Response, Form
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
from app.src.controller import run_backend
from .data.index_documents import load_to_ES

origins = ["http://frontend:80"]  # origin for deployment in docker

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize ES data
try:
    load_to_ES()
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


@app.post('/query')
def query_handler(query: str = Form(...)):
    """
    Method to handle POST requests from frontend for main functionality. In the body, query should contain the search term.
    """
    function_result = test_function(query)

    #edges = json.dumps({
    #    0: {"from": "t0", "to": "t1"},
    #    1: {"from": "t0", "to": "t2"},
    #    2: {"from": "t0", "to": "t3"},
    #    3: {"from": "t1", "to": "t4"},
    #    4: {"from": "t1", "to": "t5"},
    #})
    #papers = json.dumps({
    #    0: {"name": "p0_name", "authors": "p0_auth", "id": "p0_id"},
    #    1: {"name": "p1_name", "authors": "p1_auth", "id": "p1_id"},
    #    2: {"name": "p2_name", "authors": "p2_auth", "id": "p2_id"},
    #    3: {"name": "p3_name", "authors": "p3_auth", "id": "p3_id"},
    #    4: {"name": "p4_name", "authors": "p4_auth", "id": "p4_id"},
    #    5: {"name": "p5_name", "authors": "p5_auth", "id": "p5_id"},
    #    6: {"name": "p6_name", "authors": "p6_auth", "id": "p6_id"},
    #    7: {"name": "p7_name", "authors": "p7_auth", "id": "p7_id"},
    #    8: {"name": "p8_name", "authors": "p8_auth", "id": "p8_id"},
    #    9: {"name": "p9_name", "authors": "p9_auth", "id": "p9_id"},
    #})

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
