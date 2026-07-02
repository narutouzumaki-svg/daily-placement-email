import os
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv


load_dotenv()

EMAIL = os.getenv("EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")


def send_email(subject, html_body):

    message = MIMEMultipart("alternative")

    message["From"] = EMAIL
    message["To"] = EMAIL
    message["Subject"] = subject

    message.attach(MIMEText(html_body, "html"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:

        server.starttls()

        server.login(
            EMAIL,
            APP_PASSWORD
        )

        server.send_message(message)

    print("Email sent successfully.")