import os
import json
import google.generativeai as genai

API_KEY = os.getenv("GEMINI_API_KEY", "")
MODEL = "gemini-1.5-flash"


def call_llm(description: str):
    if not API_KEY:
        raise Exception("GEMINI_API_KEY not set")

    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel(MODEL)

    prompt = f"""
You are a transaction categorization system.

Classify the transaction into one of:
- Cloud Infrastructure
- Office Supplies
- Salaries
- Utilities
- Software
- Travel
- Miscellaneous

Return ONLY JSON in this format:
{{
  "category": "...",
  "confidence": 0.0-1.0,
  "reason": "short explanation"
}}

Transaction: {description}
"""

    response = model.generate_content(prompt)
    text = response.text

    try:
        return json.loads(text)
    except:
        return {
            "category": "Miscellaneous",
            "confidence": 0.5,
            "reason": "fallback parsing failed"
        }