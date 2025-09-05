from dotenv import load_dotenv
import os, smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
load_dotenv()

sender = os.getenv('EMAIL')
password = os.getenv('PASSWORD')
recipients = os.getenv('RECIPIENT')
SMTP_PORT = 587
SMTP_LINK = 'smtp.gmail.com'

contact_list = recipients.split(',')
distribution_list = []

for contact in contact_list:
    distribution_list.append(contact.strip())

def send_email(subject, mail_list, body):
    try:
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = ','.join(mail_list)
        message['Subject'] = subject
        content = MIMEText(body, 'plain')
        message.attach(content)
    
        with smtplib.SMTP(SMTP_LINK, SMTP_PORT) as server:
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, mail_list, message.as_string())
        print('Email successfully sent')
    except Exception as e:
        print(f'Email not sent: {e}')
         
if __name__ == '__main__':
    body = "This is another day of sending email via automation"
    mail_list = distribution_list
    subject = 'Email Automation'
    send_email(subject, mail_list, body)