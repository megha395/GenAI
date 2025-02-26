# Face to Emoji Generator

This project detects facial expressions from an image using Mediapipe's FaceMesh and maps the detected expression to a relevant emoji. It includes:
* A Python script for standalone execution
* A FastAPI server for API-based access
* A Jupyter Notebook for step-by-step analysis

## Features
* Detects facial expressions from an image
* Uses Mediapipe FaceMesh for facial landmark detection
* Maps detected expressions to relevant emoji
* Provides an API using FastAPI
* Works with only a single face image

## Project Structure
Emoji_generation/
│-- main.py  # Standalone script for face-to-emoji conversion

│-- api.py  # FastAPI server implementation
│-- notebook.ipynb  # Jupyter Notebook for interactive testing
│-- README.md  # Project documentation
│-- requirements.txt  # List of dependencies

### Installation
First, install the required dependencies:
pip install -r requirements.txt

### Usage
1. Running the FastAPI Server
Start the FastAPI server using:
uvicorn api:app --host 0.0.0.0 --port 8000
Then, open your browser or use Postman to access:
http://localhost:8000/

3️. API Endpoints
Upload an Image for Emoji Prediction
Endpoint: POST /predict Description: Upload a face image and receive an emoji prediction.
Get API Status
Endpoint: GET /

#### Emotion to Emoji Mapping

Happy: 😊
Neutral: 😐
Angry: 😡
Surprise: 😮

