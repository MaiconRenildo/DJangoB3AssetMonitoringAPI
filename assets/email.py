def send(to:str,subject:str,msg:str):
    import os,dotenv
    dotenv.load_dotenv(dotenv.find_dotenv())
    from email.message import EmailMessage
    import smtplib

    email = EmailMessage()

    email['From'] = os.getenv("EMAIL_SENDER_NAME") + " <" + os.getenv("EMAIL_SENDER_EMAIL") + ">"
    email['Subject'] = subject
    email['To'] = to

    email.set_content(msg)

    with smtplib.SMTP(os.getenv("EMAIL_HOST"),int(os.getenv("EMAIL_PORT"))) as server:
        server.login(os.getenv("EMAIL_LOGIN"),os.getenv("EMAIL_PASSWORD"))
        return server.send_message(email)