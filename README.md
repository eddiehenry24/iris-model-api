# ML Model Deployment Example

## How the Model Works

The application uses a trained Random Forest classifier to predict Iris flower species based on four measurements: sepal length, sepal width, petal length, and petal width.

When a user sends these measurements to the `/predict` endpoint, FastAPI passes them to the trained model. The model then returns a predicted flower species: setosa, versicolor, or virginica.

The API can be tested using FastAPI's interactive documentation or an HTTP request.

Complete code (including a trained model) to deploy and run inference with a machine learning model built on the Iris dataset using Docker and FastAPI.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/eddiehenry24/iris-model-api.git
cd iris-model-api
```

### 2. Start the API

```bash
docker build -t iris-model-api .
docker run --rm -p 127.0.0.1:8000:8000 iris-model-api
```

To run locally on macOS or Linux with Python 3.12, run:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 -m uvicorn server:app --port 8000
```

### 3. Send a prediction request

Keep the API running and open a second terminal. The four values are in centimeters, in this order: sepal length, sepal width, petal length, and petal width.

```bash
curl -X POST http://localhost:8000/predict \
  -H 'Content-Type: application/json' \
  -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
```

Expected response with HTTP status 200:

```json
{"predicted_class":"setosa"}
```

You can also send the same request with `python3 client.py` from the repository folder, or try it in the [interactive API docs](http://localhost:8000/docs).

## References

- [YouTube tutorial](https://www.youtube.com/watch?v=vA0C0k72-b4)
