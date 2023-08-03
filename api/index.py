from fastapi import FastAPI
from pydantic import BaseModel
import requests
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse
from typing import Dict, Any


class Request(BaseModel):
    url: str
    headers: Dict[str, str] = {}
    payload: Any = None
    params: Dict[str, str] = {}


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def docs_request():
    html_content = """
        <html>
            <head>
                <title>Request Forwarder API</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        margin: 20px;
                    }
                    h1 {
                        color: #000;
                    }
                    h2 {
                        color: #666;
                    }
                    h3 {
                        color: #666;
                    }
                    .post{
                        color:orange;
                    }
                    .get{
                        color:green;
                    }
                </style>
            </head>
            <body>
                <h1>This is the request forwarder API!</h1>
                <h2>Use <span class='post'>POST</span> '/fetch' method and pass the URL of the request to forward in the body.</h2>
                <h2>Use <span class='get'>GET</span> '/ip' method to get the IP address on which the server is running.</h2>
                <h3>Your request will be forwarded via a safe IP ;)</h3>
            </body>
        </html>
    """
    return HTMLResponse(content=html_content)


@app.get("/ip")
async def get_ip():
    response = requests.get("https://api.ipify.org/?format=json")
    return jsonable_encoder(response.json())


@app.post("/fetch/get")
async def process_request(req: Request):
    response = {}
    response["request_info"] = {}

    forwarded_response = None  # Initialize the variable before the try block
    try:
        # Pass the headers and payload to the requests.get function
        forwarded_response = requests.get(
            req.url, headers=req.headers, json=req.payload, params=req.params
        )
        response_type = (
            forwarded_response.headers.get("content-type").split(";")[0]
            if forwarded_response
            else None
        )
    except Exception as e:
        print(f"Exception in /json request - {e}")
        response["request_info"]["data"] = forwarded_response.content
        response["message"] = "Request could not be forwarded! Check the URL!"
        response["reason"] = f"{e}"
        response["success"] = False
    else:
        response["request_info"]["latency"] = forwarded_response.elapsed.total_seconds()
        response["request_info"]["status_code"] = forwarded_response.status_code
        response["success"] = True
        response["request_info"]["content_type"] = response_type

        if response_type == "application/json":
            response["request_info"]["data"] = forwarded_response.json()
        else:
            response["request_info"]["data"] = forwarded_response.text

    return jsonable_encoder(response)


@app.post("/fetch/post")
async def process_request(req: Request):
    response = {}
    response["request_info"] = {}

    forwarded_response = None  # Initialize the variable before the try block
    try:
        # Pass the headers and payload to the requests.get function
        forwarded_response = requests.post(
            req.url, headers=req.headers, json=req.payload, params=req.params
        )
        response_type = (
            forwarded_response.headers.get("content-type").split(";")[0]
            if forwarded_response
            else None
        )
    except Exception as e:
        print(f"Exception in /json request - {e}")
        response["request_info"]["data"] = forwarded_response.content
        response["message"] = "Request could not be forwarded! Check the URL!"
        response["reason"] = f"{e}"
        response["success"] = False
    else:
        response["request_info"]["latency"] = forwarded_response.elapsed.total_seconds()
        response["request_info"]["status_code"] = forwarded_response.status_code
        response["success"] = True
        response["request_info"]["content_type"] = response_type

        if response_type == "application/json":
            response["request_info"]["data"] = forwarded_response.json()
        else:
            response["request_info"]["data"] = forwarded_response.text

    return jsonable_encoder(response)
