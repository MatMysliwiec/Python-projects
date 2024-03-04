import requests
import schedule
import time
import smtplib
from email.mime.text import MIMEText

def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{url} is UP")
            return True
        else:
            print(f"{url} is DOWN. Status code: {requests.status_codes}")
            send_email(url)
            return False
    except requests.ConnectionError:
        print(f"{url} is DOWN. Connection Error.")
        send_email(url)
        return False

def send_email(url):
    sender_email = ""
    sender_password = ""
    recipient_email = ""

    subject = f"Site Down Alert: {url}"
    body = f"The website {url} is currently down"

    message = MIMEText(body)
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = recipient_email

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email,sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())

def job(url):
    print(f"Checking {url} at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    check_website(url)

if __name__ == "__main__":
    website_url = ""
    schedule.every(5).minutes.do(job,website_url)
    while True:
        schedule.run_pending()
        time.sleep(5)