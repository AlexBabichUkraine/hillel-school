import imaplib
import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase

import config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(
    recipients: list,
    mail_body: str,
    mail_subject: str,
    attachment: str = None,
):
    SERVER = config.SMTP_SERVER
    PASSWORD = config.TOKEN_API
    USER = config.USER

    msg = MIMEMultipart('alternative')
    msg['Subject'] = mail_subject
    msg['From'] = f"<Hillel student Oleksiy Babich> {USER}"
    msg['To'] = ', '.join(recipients)
    msg['Reply_To'] = USER
    msg['Return'] = USER
    msg['X-mailer'] = 'decorator'

    if attachment:
        file_exists = os.path.exists(attachment)
        if not file_exists:
            print(f"{attachment} There is no file like that")
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
    mail.login(USER, PASSWORD)
    mail.sendmail(USER, recipients, msg.as_string())
    mail.quit()


def check_mail():
    PASSWORD = config.TOKEN_API
    USERNAME = config.USER
    SERVER = config.IMAP_SERVER
    imap = imaplib.IMAP4_SSL(SERVER)
    logged_in = imap.login(USERNAME, PASSWORD)
    # print(logged_in)
    # print(logged_in[1][-1].decode())
    print(imap.select('INBOX'))
