import requests
from twilio.rest import Client
import os



OWM=  os.environ.get("API") 
api_key = os.environ.get("API_KEY") 
account_sid = os.environ.get("") 
auth_token = os.environ.get("AUTH_TOKEN") 

client = Client(account_sid, auth_token)



parameters ={
    "lat" : 21.879610,
    "lon" : -102.295227,
    "appid" : api_key,
    "cnt": 5,
}
response = requests.get(OWM,params=parameters)
response.raise_for_status()
weather_data= (response.json())

will_rain =False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code)< 00:
        will_rain =True

if will_rain:
    message = client.messages.create(
        body= "Bring an umbrella , it is going to rainy ☔" ,
        from_= "+19785950566" ,
        to="+524499903223"
    )

    print(message.status)