from email.mime.text import MIMEText
import smtplib


def send_email(email, height, average_height, count):
    # mailcatcherを利用するように変更
    from_email = "test@example.com"
    to_email = email
    subject = "Height data"
    message = "Hey there, your height is <strong>%s</strong>. <br> Average height of all is <strong>%s</strong> and that is calculated out of <strong>%s</strong> people. <br> Thanks!" % (height, average_height, count)
    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email
    smtp = smtplib.SMTP('127.0.0.1', 1025)
    smtp.ehlo()
    smtp.send_message(msg)
