import requests
import datetime
pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "fjallravensssssssfjii"
USERNAME = "blueanorak"
GRAPH_ENDPOINT =  f"{pixela_endpoint}/{USERNAME}/graphs"
VALUES_ENDPOINT = f"{pixela_endpoint}/{USERNAME}/graphs/nose"


user_pixela = {
        "c" : TOKEN ,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"

}


today = datetime.datetime.now()
#response = requests.post(url =pixela_endpoint,json = user_pixela)
#print(response.text)

#https://pixe.la/@blueanorak


graph_creation_params = {
    "id": "nose",
    "name" :"Meditation",
    "unit" :"minutes",
    "type" : "int",
    "color": "shibafu",
    
}



headers = {
    "X-USER-TOKEN": TOKEN
}

# requests.post(url = GRAPH_ENDPOINT,json = graph_creation_params, headers= headers)

value_creation_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10" 

}

check =requests.post(url=VALUES_ENDPOINT,json=value_creation_params,headers=headers)




