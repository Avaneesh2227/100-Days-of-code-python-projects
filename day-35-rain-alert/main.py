import os
import requests
from twilio.rest import Client

MY_API=os.environ.get("OWM_API_KEY")
account_sid = ''
auth_token = os.environ.get("OWM_AUTH_TOKEN")


weather_params={
    "lat":12.783840,
    "lon":80.236320,
    "appid": MY_API,
    "cnt":4
}

response=requests.get("https://api.openweathermap.org/data/2.5/forecast",params=weather_params)
response.raise_for_status()
weather_data=response.json()

def need_umbrella(weather_data):
    for i in weather_data['list']:
        if i['weather'][0]['id'] < 700:
            client = Client(account_sid, auth_token)
            message = client.messages.create(
            from_='+14706836200',
            body = 'Bring an umbrella, its going to rain',
            to = '+918838400312'
            )
            print(message.status)
            return
    return "No need"

need_umbrella(weather_data)
