# Simple Transaction Categorization API

A minimal Django REST API that calls an LLM to categorize transactions.

## What It Does

1. You send: `{"description": "AWS invoice"}`
2. It calls LLM (OpenAI or Mock)
3. Returns: `{"category": "Cloud Infrastructure", "confidence": 0.95}`

That's it!

---

## Setup (2 minutes)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Server
```bash
python manage.py runserver
```

You should see:
```
Starting development server at http://127.0.0.1:8000/
```

### 3. Test It (New Terminal)
```bash
python test.py
```

---

## API Endpoint

### POST `/api/categorize/`

**Request:**
```json
{
  "description": "AWS invoice for cloud services"
}
```

**Response:**
```json
{
  "success": true,
  "description": "AWS invoice for cloud services",
  "category": "Cloud Infrastructure",
  "confidence": 0.95
}
```

---

## Configuration

### Option 1: Use Mock (No API Key Needed) ✅
Edit `.env`:
```
LLM_PROVIDER=mock
LLM_API_KEY=
```

Run and test immediately!

### Option 2: Use OpenAI
Edit `.env`:
```
LLM_PROVIDER=openai
LLM_API_KEY=sk-your-api-key-here
```

---

## Valid Categories

- Office Supplies
- Cloud Infrastructure
- Salaries
- Utilities
- Travel
- Software
- Equipment
- Miscellaneous

---

## Files

- `settings.py` - Django config
- `urls.py` - API route
- `views.py` - API endpoint (80 lines)
- `llm_helper.py` - LLM integration (40 lines)
- `test.py` - Test script

**Total: ~150 lines of code**

---

## Example Usage

### Using curl:
```bash
curl -X POST http://localhost:8000/api/categorize/ \
  -H "Content-Type: application/json" \
  -d '{"description": "AWS invoice for cloud services"}'
```

### Using Python:
```python
import requests

response = requests.post(
    'http://localhost:8000/api/categorize/',
    json={'description': 'AWS invoice for cloud services'}
)

print(response.json())
```

---

## Testing

Run the test script:
```bash
python test.py
```

It will test 5 transactions and show results.

---

## That's It!

Simple, clean, exactly what was asked for.
