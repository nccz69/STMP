#!/usr/bin/python3
# Import Python Packages
import smtplib
# Set Global Variables
gmail_user = 'nccz69@gmail.com'
gmail_password = 'mwxmcoasqzvdowis'
# Input Informations
enter_email = input('Please enter destination address: ')
enter_subject = input('Please enter your subject: ')
enter_message = input("Please enter your message:\n")
# Create Email
mail_from = gmail_user
mail_to = enter_email
mail_subject = enter_subject
mail_message_body = enter_message

mail_message = '''\
From: %s
To: %s
Subject: %s
%s
''' % (mail_from, mail_to, mail_subject, mail_message_body)
# Sent Email
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(gmail_user, gmail_password)
server.sendmail(mail_from, mail_to, mail_message)
server.close()