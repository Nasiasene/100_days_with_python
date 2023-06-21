import smtplib as smtp
EMAIL = "davi.nasiamorim366@gmail.com"
PASSWORD = "xxx"



class NotificationManager:
    
    def send_email(self, email_to, message_sub, message_body):
        conection = smtp.SMTP("smtp.gmail.com")
        conection.starttls()
        conection.login(user=EMAIL, password= PASSWORD)
        conection.sendmail(
            from_addr=EMAIL, to_addrs=email_to,
            msg=f"Subject:{message_sub}\n\n{message_body}"
        )
        conection.close()