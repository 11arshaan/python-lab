import requests
import os
from dotenv import load_dotenv

load_dotenv()

app_id = os.getenv("APP_ID")
app_key = os.getenv("APP_KEY")
sheety_url = os.getenv("SHEETY_URL")
token = os.getenv("TOKEN")
from datetime import datetime

now = datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")

headers = {
    'x-app-id': app_id,
    'x-app-key': app_key,
    'Authorization': token
}

data = {
    'query': "",
    'gender': "male",
    "weight_kg": 63.5,
    "height_cm": 182,
    "age": 27
}

exercise = input("Which exercise did you complete: ")
data['query'] = exercise
r = requests.post("https://trackapi.nutritionix.com/v2/natural/exercise", data=data, headers=headers)
print(r.json())

workout = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise,
        "duration": r.json()['exercises'][0]['duration_min'],
        "calories": r.json()['exercises'][0]['nf_calories']
    }
}
sheet = requests.post(sheety_url, json=workout, headers=headers)
print(sheet.json())
