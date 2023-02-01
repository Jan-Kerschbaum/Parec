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

from fastapi import FastAPI, Response, Form
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
from app.src.controller import run_backend

origins = ["http://frontend:80"]  # origin for deployment in docker
#origins=["*", "http://localhost:5173"]  # origins for testing locally

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    graph = json.dumps({
        0:{"from": "t0", "to": "t1"},
        1:{"from": "t0", "to": "t2"},
        2:{"from": "t0", "to": "t3"},
        3:{"from": "t1", "to": "t4"},
        4:{"from": "t1", "to": "t5"},
    })
    return Response(content=json.dumps({"result": function_result, "graph": graph}), status_code=200)

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