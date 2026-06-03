import requests

API_KEY = "YOUR_API_KEY"

url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"

params = {
    "input": "Meenakshi Mission Hospital Madurai",
    "inputtype": "textquery",
    "fields": "place_id,name,formatted_address",
    "key": API_KEY
}

response = requests.get(url, params=params)
print(response.json())