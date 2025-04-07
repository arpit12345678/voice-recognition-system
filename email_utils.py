import smtplib
from email.message import EmailMessage
from config import EMAIL_USER, EMAIL_PASS, EMAIL_HOST, EMAIL_PORT


def send_email(to, body):
    try:
        msg = EmailMessage()
        msg["From"] = EMAIL_USER
        msg["To"] = to
        msg["Subject"] = body
        msg.set_content(body)

        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_USER, EMAIL_PASS)
            smtp.send_message(msg)

        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
