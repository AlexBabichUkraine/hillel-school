import homework13_library


def main():
    recipients = ['alex2010babich@ukr.net']
    mail_body = 'Text from Dnipro'
    mail_subject = f"It's a dog \U0001F415"
    # attachment
    attachment = 'library.py'

    homework13_library.send_email(
        recipients=recipients,
        mail_body=mail_body,
        mail_subject=mail_subject,
        attachment=attachment,
    )


if __name__ == '__main__':
    main()
