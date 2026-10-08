#import random 
import pyotp
import qrcode
#pip install pyotp qrcode[pil]

def create_totp(mail):
    secret = pyotp.random_base32()
    totp = pyotp.TOTP(secret)

    uri = totp.provisioning_uri(
        name="MyApp", 
        issuer_name=mail
    )

    img = qrcode.make(uri)
    img.save("qr_code.png")

    return secret

print(create_totp("uwu")) 
 
#random.randint(1000000, 999999)
# OTP - one time password 
# TOTP - timed OTP
# Секретный ключ (sha256, rsa, ...)
# Текущее время x Секретный ключ -> 412748...
# Условие работы: Синхронизация по времени

# HOTP - по счетчику
# 0 - начальное состояние
# Нажатие кнопки, переход на страничку (любые действия)-> +1 к счетчику
# Счетчик x Секретный ключ -> 412748...