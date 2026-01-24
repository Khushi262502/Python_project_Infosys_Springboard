from typing import Dict
from email.message import EmailMessage
import smtplib

#def send_email(receiver , subject , body):
       #password = "fnnqdhcrufysesjd"

   # message = MIMEText(body)
   # message["Subject"] = subject
   # message["From"] = sender
   # message["To"] = receiver
   # server = smtplib.SMTP("smtp.gmail.com" , 587)

    #server.starttls()
    #server.login(sender , password)

    #server.sendmail(sender , receiver , message.as_string())
    #server.quit()

EMAIL="khushijuly2004@gmail.com"
PASSWORD = "fnnqdhcrufysesjd"
SMTP_SERVER ="smtp.gmail.com"
SMTP_PORT = 465
def send_email(to_mail:str , anomaly:dict):
    subject = "Log anomaly detected"
    body = f"""
            Anomaly detected in system logs
            time window: {anomaly['timestamp']}
            Error count:{anomaly['error_count']}
            Z score:{round(anomaly['z_score'],2)}
            Please review log data

            Regards,
            Khushi Singh
"""
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = EMAIL
    msg["To"] = to_mail
    msg.set_content(body)

    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        server.login(EMAIL , PASSWORD)
        server.send_message(msg)


