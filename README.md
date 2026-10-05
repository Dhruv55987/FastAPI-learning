# FastAPI Learning 🚀

This repository contains my learning journey with **FastAPI**, from the basics of creating APIs to more advanced concepts such as authentication, middleware, dependencies, and API security.

The purpose of this repository is to learn how to build modern, scalable APIs using Python and FastAPI.

---

## 📚 What I Am Learning

### 1. FastAPI Basics

* Creating a FastAPI application
* Creating API endpoints
* GET, POST, PUT, and DELETE requests
* Path parameters
* Query parameters
* Request bodies
* JSON responses
* HTTP status codes
* Running FastAPI applications
* Interactive API documentation

---

### 2. Pydantic

Learning how Pydantic is used for:

* Request validation
* Response validation
* Data models
* Type checking
* Structured API data

Example:

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
```

---

### 3. Dependency Injection

Learning how FastAPI's `Depends()` system works.

Topics include:

* Dependency functions
* Reusable dependencies
* `Depends()`
* Authentication dependencies
* Sharing common logic between endpoints

Example:

```python
from fastapi import Depends

@app.get("/users")
def get_users(user=Depends(get_current_user)):
    return user
```

---

### 4. Authentication & Authorization

Learning how to secure APIs using:

* OAuth2
* JWT
* Password hashing
* Access tokens
* Token validation
* Authentication dependencies
* Role-based access control (RBAC)

The authentication experiments are located in:

```text
Advanced_FastApi_Concepts/
└── jwt_authentication/
```

---

### 5. Middleware

Learning how middleware works in FastAPI.

Topics include:

* Request/response lifecycle
* Custom middleware
* Logging
* Processing requests before reaching endpoints
* Processing responses before returning them
* CORS

Basic flow:

```text
Client
   ↓
Middleware
   ↓
FastAPI Endpoint
   ↓
Response
   ↓
Middleware
   ↓
Client
```

---

### 6. CORS

Learning how **Cross-Origin Resource Sharing (CORS)** works and how to configure it in FastAPI.

CORS becomes important when a frontend and backend are running on different origins.

Example:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

### 7. API Documentation

FastAPI automatically provides interactive API documentation.

After starting the server:

```text
http://127.0.0.1:8000/docs
```

FastAPI provides Swagger UI for testing API endpoints.

It also provides ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

## 🗂️ Repository Structure

The repository is organized according to the concepts I am learning.

```text
FastAPI-learning/
│
├── FastApi/
│   ├── basic concepts
│   ├── API endpoints
│   ├── request handling
│   └── validation
│
├── Advanced_FastApi_Concepts/
│   ├── jwt_authentication/
│   ├── middleware/
│   ├── dependencies/
│   ├── cors/
│   └── other advanced concepts
│
├── .gitignore
├── requirements.txt
└── README.md
```

The exact structure may change as I continue learning FastAPI.

---

## 🛠️ Technologies Used

* **Python**
* **FastAPI**
* **Pydantic**
* **Uvicorn**
* **OAuth2**
* **JWT**
* **HTTP**
* **REST APIs**

---

## ⚙️ Installation

Clone the repository:

```bash
git clone <repository-url>
```

Move into the project directory:

```bash
cd FastAPI-learning
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment on Windows:

```powershell
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running FastAPI

A basic FastAPI application can be started using:

```bash
uvicorn main:app --reload
```

Here:

```text
main → Python file (main.py)
app  → FastAPI object
```

The `--reload` option automatically restarts the server when code changes.

The application will normally be available at:

```text
http://127.0.0.1:8000
```

---

## 📖 Learning Approach

This repository is not intended to be a production-ready application.

The main goal is to understand **how FastAPI works internally and how its different components fit together**.

My learning approach is:

```text
Learn Concept
     ↓
Understand Why It Is Used
     ↓
Build a Small Example
     ↓
Test the API
     ↓
Experiment / Break the Code
     ↓
Fix the Problem
     ↓
Build a Small Project
```

---

## 🎯 Current Learning Goals

* [x] FastAPI basics
* [x] API routes
* [x] Request and response handling
* [x] Pydantic
* [x] Dependencies
* [x] Middleware
* [x] CORS
* [x] JWT authentication
* [x] OAuth2 basics
* [ ] Database integration
* [ ] SQLAlchemy
* [ ] Async programming
* [ ] Testing FastAPI applications
* [ ] Dockerizing FastAPI
* [ ] Deploying FastAPI applications
* [ ] Building a complete production-style API

---

## 💡 Why FastAPI?

FastAPI is useful for building APIs and backend services in Python.

It provides:

* High performance
* Automatic API documentation
* Request validation
* Type hints
* Dependency injection
* Async support
* Easy integration with machine learning models

It is particularly useful for **ML model deployment**, where a trained model can be exposed through an API.

For example:

```text
ML Model
   ↓
FastAPI
   ↓
/predict endpoint
   ↓
Client
```

---

## 🚀 Future Projects

After learning the individual FastAPI concepts, I plan to combine them into complete projects such as:

* ML model prediction API
* Authentication system
* CRUD API
* ML inference API with authentication
* FastAPI + database application
* FastAPI + Docker deployment

---

## 👨‍💻 Author

**Dhruv Patel**

B.Tech — Electronics & Instrumentation Engineering
SGSITS, Indore

Interested in:

* Machine Learning
* Deep Learning
* Generative AI
* Backend Development
* MLOps
* Robotics

---

## ⭐ Purpose of This Repository

This repository serves as a personal reference and record of my **FastAPI learning journey**, experiments, and projects.

The goal is not just to memorize FastAPI syntax, but to understand **how APIs, authentication, middleware, dependencies, and backend systems work together**.

│
└── README.md
