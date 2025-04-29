import smtplib
import datetime as dt
import random


my_email = "testingzhang521@gmail.com"
password= "akae lqjt apuv fkvb"


date = dt.datetime.now()
day_week = date.weekday()



if day_week == 6:
    with open(r"Day 32\quotes.txt", "r", encoding = "utf-8") as list_quotes:
       list_quotes=  [line.strip() for line in list_quotes if line.strip()]
       quote = random.choice(list_quotes)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user= my_email , password=password )
        connection.sendmail(
            from_addr= my_email,
            to_addrs= "zirwhe@gmail.com",
            msg= f"Subject: Sunday phrase \n\n {quote}"

        )