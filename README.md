# Iris Flower Prediction App

This repository contains a machine learning application for predicting the class of Iris flowers based on input features. The application consists of two main components:

1. **Backend**: A FastAPI application that serves the ML model for predictions.
2. **Frontend**: A Streamlit application for user interaction and visualization.

## Setup and Installation

### Backend Setup

The backend is containerized using Docker. Follow these steps to set up and run the backend:

#### 1. **Pull the Docker Image**

```bash
docker build -t iris-fastapi-app .
docker run -d -p 3000:8000 /iris-fastapi-app:latest
```

### Frontned Setup

#### 1. clone the git repo

```bash
git clone https://github.com/Gruhit13/deployment_week15.git
cd deployment_week15
```

#### 2. **Install the dependencies**

```bash
pip install -r requirements.txt
```

#### 3. **Launch the frontend**

```bash
streamlit run frontend.py
```
