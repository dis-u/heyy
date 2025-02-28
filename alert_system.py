import smtplib

def send_email_alert(message):
    sender = "your_email@gmail.com"
    recipient = "admin_email@gmail.com"
    password = "your_password"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, recipient, f"Subject: IDS Alert\n\n{message}")
    server.quit()
