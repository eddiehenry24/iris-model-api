# ML Model Deployment Example

Complete code (including a trained model) to deploy and run inference with a machine learning model built on the Iris dataset using Docker and FastAPI.

## Getting Started

### 1. Navigate to the repository

Open a terminal and navigate to the root of this repository.

### 2. Build the Docker image

```bash
docker build -t image_name .
```

### 3. Run the container

```bash
docker run --name container_name -p 8000:8000 image_name
```

### 4. Open the application

The terminal output should include:

```text
INFO:     Uvicorn running on http://0.0.0.0:8000
```

Open `http://localhost:8000/docs` in your browser to test the model using the FastAPI interactive interface.

### 5. Query the model

**Via the web interface:** Open `http://localhost:8000/docs` to test the model.

**Via the Python client:** Run `client.py`.

**Via a curl request:**

```bash
curl -X POST "http://localhost:8000/predict" -H "accept: application/json" -H "Content-Type: application/json" -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
```

## References

- [YouTube tutorial](https://www.youtube.com/watch?v=vA0C0k72-b4)
