from datetime import datetime
import smtplib

my_email = "hlearnstuff@gmail.com"
password = ""
message = "Subject:Hello\n\nThis is the body of my email."

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls() # encrypts the connection
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="harshaan.work@gmail.com", msg=message)
connection.close()

