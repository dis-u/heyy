import logging

logging.basicConfig(filename="logs/alerts.log", level=logging.INFO)

def log_alert(message):
    logging.info(message)
