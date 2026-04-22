
```markdown
# 📊 AI-Powered Transaction Categorization API

## 📌 Overview

This project is a backend-only AI-powered transaction categorization service built using **Django REST Framework** and an **LLM (Google Gemini)**.

The system automatically classifies financial transactions into predefined categories using contextual understanding from an LLM.

---

## 🚀 Features

- REST API built with Django
- LLM-powered transaction classification
- Structured JSON response
- Deterministic output format
- Clean service-based architecture
- Simple test client for API validation

---

## 🏗️ Architecture

```

Client (Postman / test.py)
↓
Django REST API (views.py)
↓
LLM Service Layer (llm.py)
↓
Google Gemini API
↓
Structured JSON Response

```

---

## 📂 Project Structure

```
simple_categorizer/
│
├── manage.py
├── settings.py
├── urls.py
├── test.py
│
├── api/
│ ├── views.py # API endpoint
│ ├── llm.py # LLM integration layer
│ ├── __init__.py
│
└── .env # API keys (not committed)

````

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/transaction-categorizer.git
cd transaction-categorizer
````

---

### 2. Create virtual environment

```bash
python -m venv .venv
```

Activate:

**Windows:**

```bash
.venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install django djangorestframework google-generativeai python-dotenv
```

---

### 4. Configure environment variables

Create a `.env` file in root:

```env
GEMINI_API_KEY=your_api_key_here
```

---

### 5. Run migrations (if required)

```bash
python manage.py migrate
```

---

### 6. Start server

```bash
python manage.py runserver
```

Server runs at:

```
http://127.0.0.1:8000/
```

---

## 📡 API Endpoint

### 🔹 Categorize Transaction

```
POST /api/categorize/
```

---

### 📥 Request Body

```json
{
  "description": "AWS cloud invoice for production servers"
}
```

---

### 📤 Response

```json
{
  "predicted_category": "Cloud Infrastructure",
  "confidence_score": 0.95,
  "explanation": "AWS is a cloud service provider used for infrastructure"
}
```
<img width="1795" height="926" alt="image" src="https://github.com/user-attachments/assets/156e158f-4404-42d2-86c6-dc589e5ef297" />


## 🧪 Testing the API

### Option 1: Postman

1. Open Postman
2. Create new request
3. Method: `POST`
4. URL:

```
http://127.0.0.1:8000/api/categorize/
```

5. Body → raw → JSON:

```json
{
  "description": "Microsoft 365 subscription payment"
}
```

6. Click **Send**

---

### Option 2: Python Test Script

Run:

```bash
python test.py
```

This script sends multiple sample transactions and prints categorized results.

---

## 📊 Sample Categories

The system classifies transactions into:

* Cloud Infrastructure
* Office Supplies
* Salaries
* Utilities
* Software
* Travel
* Miscellaneous

---

## 🧠 Design Decisions

* LLM used for semantic classification (no training required)
* Strict JSON output enforced for consistency
* Lightweight architecture (no database, no vector store)
* Service layer separation for scalability

---

## ❗ Notes

* No database is used (as per assignment scope)
* No model training is required
* LLM fallback logic is used if API fails
* Designed for simplicity and clarity

---

## 👨‍💻 Tech Stack

* Python
* Django
* Django REST Framework
* Google Gemini API
* dotenv

---

## 📌 Author

Built as a backend engineering exercise for AI-powered transaction classification.

---

## ✅ Status

✔ Working API
✔ LLM integration
✔ Structured output
✔ Testable via Postman / script

```


✔ Resume bullet points from this project  
✔ Or polish GitHub repo to look production-grade  

Just tell 👍
```




