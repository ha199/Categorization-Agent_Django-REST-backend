import requests

url = "http://127.0.0.1:8000/api/categorize/"

tests = [
    "AWS cloud bill",
    "Office chair purchase",
    "Salary payment to employee",
    "Electricity bill",
    "Zoom subscription"
]

for t in tests:
    res = requests.post(url, json={"description": t})
    print(t, "=>", res.json())