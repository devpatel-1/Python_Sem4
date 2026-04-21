import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Sender and receiver details
sender_email = "devapatel09092006@gmail.com"
receiver_email = "24012011080@gnu.ac.in"
password = "vlfejjevwjkfeprvzkhlhvkca"

# Create message object
msg = MIMEMultipart()
msg['Subject'] = "Test Email with JPEG Attachment"
msg['From'] = sender_email
msg['To'] = receiver_email

# Email body
body = "Hello! This is a test email with JPEG attachment."
msg.attach(MIMEText(body, 'plain'))

# Open and attach JPEG file
with open("image.jpeg", "rb") as file:
    img = MIMEImage(file.read(), name="image.jpeg")
    msg.attach(img)

# Connect to SMTP server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

# Login
server.login(sender_email, password)

# Send email
server.send_message(msg)

# Close server
server.quit()

print("Email sent successfully!")
