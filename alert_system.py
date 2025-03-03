
import psutil

def get_alerts():
    alerts = []
    for conn in psutil.net_connections(kind='inet'):
        if conn.status == 'SYN_SENT' or conn.status == 'TIME_WAIT':
            alerts.append({"time": "Real-time", "message": f"Potential threat from {conn.raddr.ip}:{conn.raddr.port}"})
    return alerts

import smtplib

def send_email_alert(message):
    sender = "harsh06harshitha@gmail.com"
    recipient = "116harshharshitha@gmail.com"
    password = "harshharsh04"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, recipient, f"Subject: IDS Alert\n\n{message}")
    server.quit()
