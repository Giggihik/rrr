import smtplib
from email.message import EmailMessage


def send_email(to_email, subject, body):
    my_email = "giggihik@gmail.com"
    my_password = "dmag ppqd szgp mhfp" 

    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = my_email
    msg["To"] = to_email

    with open("qr_code.png", "rb") as f:
        msg.add_attachment(f.read(), maintype="image", subtype="png", filename="qr_code.png")
    try:
        print("Отправка письма...")
      
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            # server.set_debuglevel(1) 
            # server.ehlo()
            server.starttls()  
            server.ehlo()
            server.login(my_email, my_password)
            server.send_message(msg)
            print("[УСПЕХ] Письмо отправлено!")
    except Exception as e:
        print("Не получилось")
        print(f"Причина ошибки: {e}")  

send_email(
    to_email="patdesathonor6@gmail.com",
    subject="6767",
    body="qr_code"  
)
