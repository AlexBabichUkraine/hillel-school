import os
import smtplib
from email import encoders

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import
from typing import List


def send_email(
    *,
    recipients: List[str],
    mail_body: str,
    mail_subject: str,
    attachment: str = None,
):
    server = config.SMTP_SERVER
    password = config.TOKEN_API
    user = config.USER
    msg = MIMEMultipart('alternative')
    msg['Subject'] = mail_subject
    msg['From'] = f'<Lesson 13 user {user}>'
    msg['To'] = ', '.join(recipients)
    msg['Reply-To'] = user
    msg['Return-Path'] = user
    msg['X-Mailer'] = 'decorator'
    if attachment:
        file_exists = os.path.exists(attachment)
        if not file_exists:
            print(f"file {attachment} does not exist")
        else:
            basename = os.path.basename(attachment)
            filesize = os.path.getsize(attachment)
            file = MIMEBase('application', f'octet-stream; name={basename}')
            file.set_payload(open(attachment, 'rb').read())
            file.add_header('Content-Description', attachment)
            file.add_header('Content-Description', f'attachment; filename={attachment}; size={filesize}')
            encoders.encode_base64(file)

            msg.attach(file)

    text_to_send = MIMEText(mail_body, 'plain')
    msg.attach(text_to_send)


mail = smtplib.SMTP_SSL(SERVER)
mail.login(user=, password=)
mail.sendmail(recipients, msg.as_string())
mail.quit()
