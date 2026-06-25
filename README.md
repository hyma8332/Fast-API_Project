# AI Text Processing REST API

A REST API built using **FastAPI** that provides AI-powered text processing services, including:

- Text Summarization
- Text Translation
- Email Generation

The project follows a clean and modular architecture with request validation, exception handling, logging, environment variable configuration, and automatically generated API documentation.

---

## Features

- FastAPI framework
- RESTful API design
- Request validation using Pydantic
- Global exception handling
- Logging support
- Environment variable management using `.env`
- Automatic API documentation (Swagger UI & ReDoc)
- Modular and scalable project structure

---

## Project Structure

```
ai_api_project/
│
├── app/
│   ├── main.py
│   ├── routes/
│   ├── services/
│   ├── models/
│   ├── core/
│   └── exceptions/
│
├── .env
├── requirements.txt
└── README.md
```

---

## Installation

### Clone the repository

```bash
git clone <repository-url>
cd ai_api_project
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The server will start at:

```
http://127.0.0.1:8000
```

---

## API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## API Endpoints

### 1. POST /summarize

Summarizes the provided text.

**Request**

```json
{
  "text": "Artificial Intelligence is transforming industries worldwide..."
}
```

**Response**

```json
{
  "summary": "Artificial Intelligence is transforming industries..."
}
```

---

### 2. POST /translate

Translates text into the specified language.

**Request**

```json
{
  "text": "Hello",
  "target_language": "French"
}
```

**Response**

```json
{
  "translated_text": "Bonjour"
}
```

---

### 3. POST /generate-email

Generates a professional email based on the provided details.

**Request**

```json
{
  "recipient_name": "Manager",
  "purpose": "Leave Request"
}
```

**Response**

```json
{
  "email": "Dear Manager,\n\nI hope you are doing well..."
}
```

---

## Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn
- Python-dotenv

---

## Error Handling

The application includes centralized exception handling to provide consistent and user-friendly error responses.

---

## Logging

Logging is configured to record application events, API requests, and errors, making debugging and monitoring easier.

---

## Environment Variables

Create a `.env` file in the project root.

Example:

```env
APP_NAME=AI API Service
VERSION=1.0
```

---

## Future Enhancements

- Integrate Hugging Face Transformer models for advanced summarization and translation.
- Add authentication using JWT.
- Connect to a database for storing request history.
- Dockerize the application for deployment.
- Add unit and integration tests.

---

## Author

Developed as part of an AI/ML Internship REST API Assignment using FastAPI.