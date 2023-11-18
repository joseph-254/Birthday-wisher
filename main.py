
import smtplib
import datetime as dt
import pandas
import random

birthday_frame = pandas.read_csv("birthdays.csv")


now = dt.datetime.now()
check_month = now.month
check_day = now.day

            #---------getting the actual month and day------#
data_by_month = birthday_frame[birthday_frame.month == check_month]
month_dict = data_by_month.to_dict()
name_in_month = month_dict["name"]


data_by_day = birthday_frame[birthday_frame.day == check_day]
day_dict = data_by_day.to_dict()
name_in_day = day_dict["name"]


    #---comparing if the details by name match---#
if name_in_month == name_in_day:
    birthday_person_name = data_by_day.name
    name = birthday_person_name.astype(str).tolist()

    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter:
        content = letter.read()
        birthday_letter = content.replace("[NAME]", name[0])


        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user="joeking6447@gmail.com", password="ngbp tyhd vhlt ehil")
        connection.sendmail(from_addr="joeking6447@gmail.com",
                            to_addrs="jkamanga56@yahoo.com",
                            msg=f"subject:Birthday Wish\n\n{birthday_letter}")



