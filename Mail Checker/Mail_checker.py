import imaplib
import getpass
import time


def check_email_imap(username, password, server, port=993):
    try:
        mail = imaplib.IMAP4_SSL(server, port)
        mail.login(username, password)
        mail.select("inbox")
        result, data = mail.search(None, "UNSEEN")

        if result == "OK":
            email_ids = data[0].split()
            if email_ids:
                print(f"You have {len(email_ids)} unread messages")
                for email_id in email_ids:
                    result, message_date = mail.fetch(email_id, "(RFC822)")
                    if result == "OK":
                        print(f"Email {email_id}")
        mail.logout()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    username = input("Enter your email address: ")
    password = input("Enter your email password: ")
    server = input("Enter your email server (e.g. imap.gmail.com): ")
    try:
        port = int(input("Enter the server port (press Enter for default port = 993): "))
    except ValueError:
        port = 993
    interval = int(input("Enter the interval for checking emails in seconds: "))

    try:
        while True:
            check_email_imap(username, password, server, port)
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Mail checker stopped")
