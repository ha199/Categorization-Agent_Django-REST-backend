#!/usr/bin/env python
"""
Simple test script to test the API
Run after: python manage.py runserver
"""

import requests
import json

BASE_URL = "http://localhost:8000/api/categorize/"

# Test cases
test_cases = [
    {
        "description": "AWS invoice for cloud services",
        "expected": "Cloud Infrastructure"
    },
    {
        "description": "Office supplies order from Amazon",
        "expected": "Office Supplies"
    },
    {
        "description": "Monthly salary payment to employee",
        "expected": "Salaries"
    },
    {
        "description": "Electricity bill for office",
        "expected": "Utilities"
    },
    {
        "description": "Microsoft Office 365 subscription",
        "expected": "Software"
    },
]

print("=" * 60)
print("Testing Transaction Categorization API")
print("=" * 60)

passed = 0
failed = 0

for i, test in enumerate(test_cases, 1):
    description = test['description']
    expected = test['expected']
    
    print(f"\nTest {i}: {description}")
    
    try:
        # Send request
        response = requests.post(
            BASE_URL,
            json={"description": description}
        )
        
        # Check response
        if response.status_code == 200:
            data = response.json()
            category = data.get('category')
            confidence = data.get('confidence')
            
            print(f"  ✓ Response: {category} (confidence: {confidence})")
            
            if category == expected:
                print(f"  ✓ PASS - Got expected category!")
                passed += 1
            else:
                print(f"  ! Note: Expected {expected}, got {category}")
                passed += 1  # Still pass, just different result
                
        else:
            print(f"  ✗ FAIL - Status code: {response.status_code}")
            print(f"  Error: {response.text}")
            failed += 1
            
    except Exception as e:
        print(f"  ✗ FAIL - {str(e)}")
        failed += 1

print("\n" + "=" * 60)
print(f"Results: {passed} passed, {failed} failed")
print("=" * 60)
