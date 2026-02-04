from email.message import EmailMessage
from app1 import password
import ssl
import smtplib

email_sender ="vzothapa333@gmail.com"
email_password= password

email_receiver =""

subject ="Email sendere test"

body =""" 
when you watch shit you do shit
"""

em = EmailMessage()
em['From'] = email_sender
em["To"] = email_receiver
em["subject"] =subject
em.set_content(body)