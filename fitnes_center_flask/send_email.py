import smtplib, ssl



from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def add(x, y):
    return x + y


@app.task
def send_email(**kwargs):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "alkost198333@gmail.com"
    receiver_email = "alkost198333@gmail.com"
    password = input("Type your password and press enter:")
    message = """\
    Subject: Hi there
    
    This message is sent from Python."""

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)