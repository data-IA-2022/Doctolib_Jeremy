import requests
from django.conf import settings

def send_mail_with_mailgun(subject, text, to_email):
    return requests.post(
        f"https://api.mailgun.net/v3/{settings.MAILGUN_DOMAIN}/messages",
        auth=("api", settings.MAILGUN_API_KEY),
        data={"from": f"noreply@{settings.MAILGUN_DOMAIN}",
              "to": [to_email],
              "subject": subject,
              "text": text})