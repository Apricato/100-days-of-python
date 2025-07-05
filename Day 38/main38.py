import requests
from datetime import datetime
import os



APP_ID = os.environ.get("API_ID")
API_KEY = os.environ.get("API_KEY")
API_ENDPOINT = os.environ.get("API_ENDPOINT")
SHEETY = os.environ.get("SHEETY")
BEARER_KEY = os.environ.get("BEARER_KEY")

headers = {
    "x-app-id" : APP_ID ,
    "x-app-key" : API_KEY
}
nutrition_params = {
    
    "query": input("How much did you excercise today and what kind of activity was it?")

}

check= requests.post(url=API_ENDPOINT,json=nutrition_params,headers=headers )
results= check.json()

exercise = results["exercises"][0]

sheety_params = {
    "workout": {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "time": datetime.now().strftime("%H:%M:%S"),
        "exercise": exercise["name"].title(),
        "duration": exercise["duration_min"],
        "calories": exercise["nf_calories"]
    }
}

special_headers ={
    "Authorization": BEARER_KEY
}
sheet= requests.post(url=SHEETY, json=sheety_params, headers=special_headers)
print(sheet.text)
