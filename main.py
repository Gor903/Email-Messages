import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()


def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    msg['from'] = user = os.getenv('SENDER_EMAIL_ACCOUNT')
    password = os.getenv('EMAIL_PASSWORD')

    server = smtplib.SMTP(
        os.getenv('YOUR_SMTP_SERVER.COM'),
        int(os.getenv('SMTP_PORT'))
    )

    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()