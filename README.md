# 🚀 FastAPI Learning

This repository contains my **FastAPI learning journey**, where I am learning how to build APIs and backend applications using Python and FastAPI.

The repository starts with the fundamentals of FastAPI and gradually moves toward more advanced concepts such as API development, authentication, dependencies, middleware, and testing.

The main goal is not just to memorize FastAPI syntax, but to understand **how APIs work and how the different components of a backend application fit together**.

---

## 📚 What I'm Learning

### 🔹 FastAPI Basics

Learning the fundamentals of creating APIs with FastAPI, including:

* Creating a FastAPI application
* API routes
* HTTP methods
* Path parameters
* Query parameters
* Request bodies
* Response handling
* Pydantic models
* API validation
* HTTP status codes
* Interactive API documentation

---

## 🔹 Building APIs

The `BuildingApi` folder contains my experiments and examples related to building APIs with FastAPI.

The focus is on understanding how a client communicates with a backend through HTTP.

Basic flow:

```text
Client
   ↓
HTTP Request
   ↓
FastAPI
   ↓
API Endpoint
   ↓
Business Logic
   ↓
HTTP Response
   ↓
Client
```

---

## 🔹 Advanced FastAPI Concepts

The `Advanced_FastApi_Concepts` folder contains more advanced concepts that I learned after understanding the basics.

Topics include:

* Dependency Injection
* `Depends()`
* Middleware
* CORS
* Authentication
* Authorization
* OAuth2
* JWT authentication
* Password hashing
* Access tokens
* Role-based access control

### Authentication Flow

```text
Client
   ↓
Login
   ↓
FastAPI
   ↓
Verify Credentials
   ↓
Generate JWT
   ↓
Client
   ↓
Send JWT with Request
   ↓
Authentication Dependency
   ↓
Protected Endpoint
```

---

## 🔹 Unit Testing

The `Unit-testing` folder contains my learning and experiments related to **testing FastAPI applications**.

The goal is to understand how API endpoints can be tested automatically instead of manually testing every endpoint.

Basic idea:

```text
Test
 ↓
Send Request
 ↓
FastAPI Endpoint
 ↓
Response
 ↓
Check Expected Result
```

---

## 📁 Repository Structure

```text
FastAPI-learning/
│
├── Advanced_FastApi_Concepts/
│   └── Advanced FastAPI concepts
│
├── BuildingApi/
│   └── API development examples
│
├── Unit-testing/
│   └── FastAPI testing
│
└── README.md
```

The repository structure will continue to evolve as I learn more FastAPI concepts.

---

## 🛠️ Technologies

* Python
* FastAPI
* Pydantic
* Uvicorn
* OAuth2
* JWT
* HTTP / REST APIs
* Pytest

---

## ⚙️ Setup

Clone the repository:

```bash
git clone https://github.com/Dhruv55987/FastAPI-learning.git
```

Move into the repository:

```bash
cd FastAPI-learning
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running a FastAPI Application

A FastAPI application can be started using Uvicorn:

```bash
uvicorn main:app --reload
```

Where:

```text
main → Python file containing the application
app  → FastAPI application object
```

The API can then be accessed at:

```text
http://127.0.0.1:8000
```

### Interactive API Documentation

FastAPI automatically provides Swagger UI:

```text
http://127.0.0.1:8000/docs
```

And ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

## 🧠 My Learning Approach

I am using this repository to learn concepts by **writing code, experimenting, debugging, and testing** rather than only following tutorials.

My learning process:

```text
Learn a Concept
       ↓
Understand Why It Is Needed
       ↓
Implement It
       ↓
Run & Test It
       ↓
Break Things
       ↓
Debug the Errors
       ↓
Understand the Solution
       ↓
Build Something With It
```

The purpose is to become comfortable enough with FastAPI that I can start a project from a problem statement and use documentation to figure out the implementation.

---

## 🎯 Learning Progress

* [x] FastAPI fundamentals
* [x] API routes
* [x] HTTP methods
* [x] Path parameters
* [x] Query parameters
* [x] Request bodies
* [x] Pydantic
* [x] API validation
* [x] Dependency Injection
* [x] `Depends()`
* [x] Middleware
* [x] CORS
* [x] OAuth2
* [x] JWT Authentication
* [x] Authorization
* [x] Unit Testing
* [ ] Database integration
* [ ] SQLAlchemy
* [ ] Async database operations
* [ ] Docker
* [ ] Deployment
* [ ] Production-ready FastAPI project

---

## 💡 Why FastAPI?

FastAPI is a modern Python web framework for building APIs. It provides features such as type-based validation, automatic API documentation, dependency injection, and support for asynchronous programming.

I am also learning FastAPI because it is useful for **Machine Learning and AI model deployment**.

For example:

```text
Trained ML Model
      ↓
   FastAPI
      ↓
 /predict endpoint
      ↓
Client Application
```

This allows a trained machine learning model to be exposed as an API that can be consumed by other applications.

---

## 🚀 Future Goals

After completing the fundamentals and advanced concepts, I plan to use FastAPI to build complete projects involving:

* ML model deployment
* CRUD APIs
* Authentication systems
* Database integration
* AI/ML inference APIs
* FastAPI + Docker
* Production-style backend applications

---

## 👨‍💻 About

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

This repository is a record of my **FastAPI learning journey**.

Rather than treating it as a finished project, I use it as a place to:

* Practice concepts
* Experiment with code
* Understand errors
* Test different approaches
* Build small examples
* Gradually move toward complete backend applications

