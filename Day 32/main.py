import smtplib
import datetime as dt

my_email = "testingzhang521@gmail.com"
password= "akae lqjt apuv fkvb"


with  smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user= my_email , password = password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs= "zirwhe@gmail.com",
        msg= "Subject: Hello from the other side \n\n Been ages has it not been ages ?"
        )



now = dt.datetime.now()
print(now)
print(now.month)