import homework13_library


def main():
    recipients = ['alex2010babich@ukr.net']
    mail_body = 'Please see my configuration file in attachment'
    mail_subject = f"Here is my 'config.py' file"
    attachment = 'config.py'

    homework13_library.send_email(
        recipients=recipients,
        mail_body=mail_body,
        mail_subject=mail_subject,
        attachment=attachment,
    )


homework13_library.check_mail()

if __name__ == '__main__':
    main()
