"""
Implements FastAPI App, which listens on port 8000 for requests from the frontend. Will need to trigger other Python components from here, ideally.
Needs to be started seperately from the frontend itself. In the finished product, this will be handeled by the docker container.

App routes:
    /
        For quick testing that the app is indeed running
    /query
        Main access point for intended functionality
"""

from fastapi import FastAPI, Response, Form
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json

origins = ["http://localhost:8080", "http://localhost:8000/query"]

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
    return Response(content=json.dumps({"result": function_result}), status_code=200)

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