import requests
from datetime import datetime
from smtplib import SMTP

MY_LAT=12.783840
MY_LONG=80.236320

def close():
    response1 = requests.get(url="http://api.open-notify.org/iss-now.json")  # this is the api endpoint
    response1.raise_for_status()  # to handle exceptions
    data1 = response1.json()
    iss_latitude = float(data1["iss_position"]["latitude"])
    iss_longitude = float(data1["iss_position"]["longitude"])
    return True if abs(iss_latitude-MY_LAT)<=5 and abs(iss_longitude-MY_LONG)<=5 else False



def night():
    parameters={
        'lat':MY_LAT,
        'lng':MY_LONG,
        'tzid':'Asia/Kolkata',
        'formatted':0
    }

    response2=requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
    response2.raise_for_status()
    data2=response2.json()
    sunrise=int(data2['results']['sunrise'].split('T')[1].split(':')[0])
    sunset=int(data2['results']['sunset'].split('T')[1].split(':')[0])
    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True
    return False

if close() and night():
    connection=SMTP("smtp.ethereal.email",port=587)
    connection.starttls()
    connection.login('eino.lesch@ethereal.email','2AFwzem9mA3RdUt2SU')
    connection.sendmail(from_addr='eino.lesch@ethereal.email',to_addrs='bobby@gmail.com',msg='Subject: Hello World \n\n'
                                                                                             'ISS is near you')


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
