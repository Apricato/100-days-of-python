##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import smtplib
import pandas as pd
import datetime
import random 
<<<<<<< HEAD
import os
=======

>>>>>>> 8583260 (Bloody Day 32)

my_email = "testingzhang521@gmail.com"
password= "akae lqjt apuv fkvb"

<<<<<<< HEAD

base_dir = os.path.dirname(os.path.abspath(__file__))


letter_1_path = os.path.join(base_dir, "letter_templates", "letter_1.txt")
letter_2_path = os.path.join(base_dir, "letter_templates", "letter_2.txt")
letter_3_path = os.path.join(base_dir, "letter_templates", "letter_3.txt")

with open(letter_1_path) as letter_one, open(letter_2_path) as letter_two, open(letter_3_path) as letter_three:
    letters = letter_one.read(), letter_two.read(), letter_three.read()
=======
with open ( "Day 32/birthday-wisher-extrahard-start/letter_templates/letter_1.txt")  as letter_one, open ("Day 32/birthday-wisher-extrahard-start/letter_templates/letter_2.txt") as letter_two, open("Day 32/birthday-wisher-extrahard-start/letter_templates/letter_3.txt") as letter_three: 
        letters = letter_one.read(), letter_two.read(), letter_three.read()
>>>>>>> 8583260 (Bloody Day 32)

current_date = datetime.datetime.now()

today = (current_date.month, current_date.day)
<<<<<<< HEAD


birthdays_csv_path = os.path.join(base_dir, "birthdays.csv")

df = pd.read_csv(birthdays_csv_path)  # Use the dynamically constructed path
=======
print (today )

df = pd.read_csv(r"Day 32\birthday-wisher-extrahard-start\birthdays.csv")
print (df)
>>>>>>> 8583260 (Bloody Day 32)

birthdays = [ {'name': row['name'], 'email': row['email']}  for index, row in df.iterrows() if (row['month'], row['day']) == today]


for person in birthdays :
          letter= random.choice(letters)
          custom_letter = letter.replace("[NAME]", person["name"])
          with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user= my_email , password=password )
            connection.sendmail(
                from_addr= my_email,
                to_addrs= person['email'],
                msg= f"Subject: HAPPY  BIRTHDAY  \n\n {custom_letter}"

            )
<<<<<<< HEAD


=======
        
        
>>>>>>> 8583260 (Bloody Day 32)


