import smtplib
from email.mime.text import MIMEText
from config import password

def send_email(sender_email, receiver_email, subject, message):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    username = 'bolgrakov@gmail.com'
    password = password

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(username, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print('Email sent successfully!')
    except Exception as e:
        print('An error occurred while sending the email:', str(e))


