from email.mime.multipart import MIMEMultipart

# *** To be imported later
from email.mime.text import MIMEText

# *** To be imported later
from email.mime.image import MIMEImage

# *** To be imported later
from pathlib import Path

# *** To be imported later
import smtplib


message = MIMEMultipart()
message["from"] = "Vincent Oke"
message["to"] = "vintestvin5@gmail.com"
message["subject"] = "This is a test from Python"
message.attach(MIMEText("Body", "plain"))
message.attach(MIMEImage(Path("pic.jpg").read_bytes()))


with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("vintestvin5@gmail.com", "pwcmjjmwgnvpxfws")
    smtp.send_message(message)
    print("Sent...")