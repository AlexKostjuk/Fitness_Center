import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp_server = "smtp.gmail.com"
smtp_port = 587
email_username = "alkost198333@gmail.com"
email_password = "jkzv lbdn qlrw emsa"

from_email = "alkost198333@gmail.com"
to_email = "alkost1983333@outlook.com"
subject = "alarm Temp"
body = f"temp CP = ."

msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(email_username, email_password)
    server.send_message(msg)
    print(f"Лист успішно відправлений!  {to_email}")
except Exception as e:
    print(f"Помилка: {e}")
finally:
    server.quit()