# -*- coding: utf-8 -*-
"""PYTHON_CAPSTONE.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19FRyZxuXlPbNlkgbDqSWQNWNJsa4Zkg2
"""

import random
import smtplib
from email.message import EmailMessage

def generate_otp():
    #Generates a random 6-digit OTP.
    otp = random.randint(100000, 999999)
    return str(otp)

email = 'saisrikarkokku7674@gmail.com'

def send_otp_to_email(email, otp):
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  from_mail = 'saisrikarkokku7674@gmail.com'
  server.login(from_mail,'enter your app created Password')
  to_mail = input("Enter your email: ")
  msg = EmailMessage()
  msg['Subject'] = 'OTP Verification'
  msg['From'] = from_mail
  msg['To'] = to_mail
  msg.set_content(f'Your OTP is {otp}')
  server.send_message(msg)
  print('Email sent')
  print(f"Sending OTP {otp} to {email}...")

def get_user_otp():
    Recived_otp = input("Enter the OTP received in your email: ")
    return Recived_otp

def verify_otp(get_user_otp, generated_otp):
    """Verifies if the entered OTP matches the generated OTP."""
    if get_user_otp == generated_otp:
        return True
    else:
        return False

def otp_verification_system():
    # this is Main function to handle OTP verification system logic
    Email = to_mail
    generated_otp = generate_otp()
    send_otp_to_email(email, generated_otp)

    attempts = 3  # Number of attempts for entering OTP
    while attempts > 0:
        user_otp = get_user_otp()
        if verify_otp(user_otp, generated_otp):
            print("Access Granted!")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect OTP. You have {attempts} attempt(s) left.")
            else:
                print("Access Denied. Too many incorrect attempts.")

if __name__ == "__main__":
    otp_verification_system()