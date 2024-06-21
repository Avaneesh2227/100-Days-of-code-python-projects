import smtplib
import random
my_email='kendra.blanda@ethereal.email'
password='MEa6u21xkUr21BWeMe'


def send_email(message,to_address):
    #with open('quotes.txt') as quotes:
        #data=quotes.readlines()
        #quote=random.choice(data)
    with smtplib.SMTP('smtp.ethereal.email',port=587) as connection:
        #way to connect to our email provider's smtp email server
        #we must provide location of our email provider's smtp server
        connection.starttls()#tls= Transport Layer Security, basically this line encrypts the email
        connection.login(user=my_email,password=password) #start a connection
        #connection.connect("smtp.ethereal.email", 587)
        connection.sendmail(from_addr=my_email,to_addrs=to_address,msg=f'Subject:Quote\n\n {message}')


'''
import datetime as dt

now=dt.datetime.now()
year=now.year
month=now.month
day_of_week=now.weekday()
print(day_of_week)
'''



##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
now=dt.datetime.now()
month=now.month
day=now.day

import pandas as pd
df=pd.read_csv('birthdays.csv')
data=df.loc[(df['month']==month) & (df['day']==day)]
dict={row['name']:row['email'] for index,row in data.iterrows()}
print(dict)

import random
for j in dict:
    choice=random.randint(1,3)
    wish=''
    with open(f'letter_templates/letter_{choice}.txt') as letter:
        for i in letter:
            wish+=i
    final_wish=wish.replace('[NAME]',j)
    send_email(final_wish,dict[j])




