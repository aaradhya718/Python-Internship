import smtplib
import ssl
from email.message import EmailMessage
EMAIL= "k**@gmail.com"
APP_PASSWORD= "Enter your App Password here"
RECEIVER= "m*@gmail.com "
msg = EmailMessage()
msg["From"] = EMAIL
msg["To"] = RECEIVER
msg["Subject"] = "Hello from Python...."
msg.set_content("The email was shared by python code...")
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465, context = context) as server :
    server.login(EMAIL,APP_PASSWORD)
    server.send_message(msg)
