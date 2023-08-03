# Request Forwarder API

This is a simple FastAPI-based API that acts as a request forwarder. It allows you to send a POST request with a URL, headers, and payload, and the API will forward that request to the provided URL. Additionally, it provides a GET endpoint to get the IP address on which the server is running.

## Endpoints

### 1. `/`

This endpoint returns an HTML page providing information about the API and how to use it.

#### Method

GET

#### Response

- Content-Type: text/html

### 2. `/ip`

This endpoint retrieves the IP address of the server on which the API is running.

#### Method

GET

#### Response

- Content-Type: application/json

### 3. `/fetch`

This endpoint is used to forward requests to a provided URL.

#### Method

POST

#### Request Body

- `url` (str): The URL to which the request should be forwarded.
- `headers` (dict, optional): Headers to be included in the forwarded request.
- `payload` (any, optional): Payload (JSON data) to be included in the forwarded request.

#### Response

The response will be in JSON format and will contain information about the forwarded request.

- If the request was forwarded successfully:
  ```json
  {
    "success": true,
    "request_info": {
      "latency": (float) Latency in seconds,
      "status_code": (int) Status code of the forwarded response,
      "content_type": (str) Content type of the forwarded response,
      "data": (object) The data received in the forwarded response (JSON or HTML)
    }
  }

Certainly! Here's the README.md content for the provided FastAPI code:

markdown
Copy code
# Request Forwarder API

This is a simple FastAPI-based API that acts as a request forwarder. It allows you to send a POST request with a URL, headers, and payload, and the API will forward that request to the provided URL. Additionally, it provides a GET endpoint to get the IP address on which the server is running.

## Endpoints

### 1. `/`

This endpoint returns an HTML page providing information about the API and how to use it.

#### Method

GET

#### Response

- Content-Type: text/html

### 2. `/ip`

This endpoint retrieves the IP address of the server on which the API is running.

#### Method

GET

#### Response

- Content-Type: application/json

### 3. `/fetch`

This endpoint is used to forward requests to a provided URL.

#### Method

POST

#### Request Body

- `url` (str): The URL to which the request should be forwarded.
- `headers` (dict, optional): Headers to be included in the forwarded request.
- `payload` (any, optional): Payload (JSON data) to be included in the forwarded request.

#### Response

The response will be in JSON format and will contain information about the forwarded request.

- If the request was forwarded successfully:
  ```json
  {
    "success": true,
    "request_info": {
      "latency": (float) Latency in seconds,
      "status_code": (int) Status code of the forwarded response,
      "content_type": (str) Content type of the forwarded response,
      "data": (object) The data received in the forwarded response (JSON or HTML)
    }
  }
  
- If the request could not be forwarded:{
  "success": false,
  "request_info": {
    "data": {},
    "message": "Request could not be forwarded! Check the URL!",
    "reason": (str) Reason for the failure
  }

}

Running the API
1. Make sure you have Python and pip installed on your system.
2. Install the required packages by running:
`pip install fastapi uvicorn requests`
3. Save the provided code in a Python file, for example, main.py.
4. Run the API using uvicorn:
`uvicorn main:app --reload`
5. The API will start running locally on http://127.0.0.1:8000.

Usage
Open your web browser and navigate to http://127.0.0.1:8000/ to access the API documentation page.
Use the provided endpoints to interact with the API as described above.
Note: The API may forward requests to the provided URL, so be cautious when using it to avoid potential security risks. It is recommended to use this API for testing purposes only and not to forward sensitive or unauthorized requests.

You can save this content to a file named `README.md` in your project directory, and it will serve as your README documentation.
