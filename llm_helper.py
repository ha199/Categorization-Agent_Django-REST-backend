import json
import os
from dotenv import load_dotenv  # ADD THIS LINE

load_dotenv()  # ADD THIS LINE - loads .env file

def call_llm(transaction_description):
    """
    Call LLM to categorize transaction.
    Returns JSON with category and confidence.
    """
    
    provider = os.getenv('LLM_PROVIDER', 'gemini')
    api_key = os.getenv('GEMINI_API_KEY', '')
    model = os.getenv('GEMINI_MODEL', 'gemini-1.5-flash')
    
    print(f"DEBUG: Provider={provider}, API Key exists={bool(api_key)}, Model={model}")
    
    # Use Mock if no API key
    if not api_key:
        print(f"⚠️ No API key configured. Using mock response.")
        return mock_categorize(transaction_description)
    
    # Call Gemini
    if provider == 'gemini':
        try:
            import google.generativeai as genai
            
            genai.configure(api_key=api_key)
            model_instance = genai.GenerativeModel(model)
            
            prompt = f"""Categorize this transaction: {transaction_description}

Valid categories: Office Supplies, Cloud Infrastructure, Salaries, Utilities, Travel, Software, Equipment, Miscellaneous

Respond ONLY with JSON: {{"category": "...", "confidence": 0.95}}"""
            
            response = model_instance.generate_content(prompt)
            content = response.text
            
            print(f"✅ LLM Response: {content}")
            
            # Extract JSON
            import re
            json_match = re.search(r'\{[^}]*\}', content)
            if json_match:
                result = json.loads(json_match.group(0))
                return result
            
            return mock_categorize(transaction_description)
            
        except Exception as e:
            print(f"❌ Gemini Error: {str(e)}. Using mock response.")
            return mock_categorize(transaction_description)
    
    return mock_categorize(transaction_description)


def mock_categorize(description):
    """Mock categorization"""
    
    description_lower = description.lower()
    
    if any(word in description_lower for word in ['aws', 'cloud', 'server', 'infrastructure']):
        return {"category": "Cloud Infrastructure", "confidence": 0.95}
    elif any(word in description_lower for word in ['office', 'supplies', 'paper', 'pen']):
        return {"category": "Office Supplies", "confidence": 0.90}
    elif any(word in description_lower for word in ['salary', 'payroll', 'wage']):
        return {"category": "Salaries", "confidence": 0.98}
    elif any(word in description_lower for word in ['electricity', 'water', 'gas', 'utility']):
        return {"category": "Utilities", "confidence": 0.92}
    elif any(word in description_lower for word in ['software', 'license', 'subscription', 'saas']):
        return {"category": "Software", "confidence": 0.88}
    elif any(word in description_lower for word in ['travel', 'flight', 'hotel', 'trip']):
        return {"category": "Travel", "confidence": 0.85}
    else:
        return {"category": "Miscellaneous", "confidence": 0.60}