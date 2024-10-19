import smtplib
from email.mime.text import MIMEText

def send_email(to_email, subject, message):
    sender_email = "your_email@gmail.com"
    password = "your_password"

    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = to_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, to_email, msg.as_string())

def create_github_issue(github_client, repo, title, body):
    return github_client.create_issue(repo, title, body)
