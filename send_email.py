import smtplib as s
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Replace with your Gmail credentials and App Password
gmail_user = 'sender@gmail.com'
gmail_password = 'your_app_password_here'

# Establish SMTP connection to Gmail's SMTP server
ob = s.SMTP('smtp.gmail.com', 587)
ob.ehlo()
ob.starttls()

try:
    # Login with your Gmail credentials
    ob.login(gmail_user, gmail_password)

    # Specify email details
    subject = "Testing mail via python"
    body = "The smtplib module defines an SMTP client session object that can be used to send mail to any internet machine with an SMTP or ESMTP listener daemon."
    message = MIMEMultipart()
    message['From'] = gmail_user
    message['To'] = "receiver1@gmail.com, receiver2@gmail.com, receiver3@gmail.com"
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Send email
    ob.sendmail(gmail_user, message['To'].split(','), message.as_string())

    print("Email sent successfully!")

except Exception as e:
    print(f"Error occurred: {e}")

finally:
    # Quit SMTP session
    ob.quit()
