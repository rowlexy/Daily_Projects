from dotenv import load_dotenv
import os, smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders # for attachments
from email.mime.base import MIMEBase # for attachments
from pathlib import Path

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

def send_email(subject, mail_list, body, attachment):
    try:
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = ','.join(mail_list)
        message['Subject'] = subject
        content = MIMEText(body, 'plain')
        message.attach(content)

        # Add attachment here
        if attachment and Path(attachment).exists():
            filename = Path(attachment).name
            with open(attachment, 'rb') as file:
                part = MIMEBase('application', 'pdf')
                part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment: filename={filename}')
            message.attach(part)
        else:
            print(f'File not found: {attachment}')
        with smtplib.SMTP(SMTP_LINK, SMTP_PORT) as server:
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, mail_list, message.as_string())
        print('Email successfully sent')
    except Exception as e:
        print(f'Email not sent: {e}')
         
if __name__ == '__main__':
    body = "This is another day of sending email via automation\nPassword to pdf file is Rowzay_27"
    mail_list = distribution_list
    subject = 'Email Automation'
    attachment = 'encrypted_testfile.pdf'
    send_email(subject, mail_list, body, attachment)