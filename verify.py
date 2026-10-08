import pyotp

def verify(secret, user_code):
    totp = pyotp.TOTP(secret)
    result = totp.verify(user_code)
    return result

secret = "44FB3DF3SLJNQSARI4XNJ2TCUEE5NZPZ"

user_code = input()
if verify(secret, user_code):
    print("Четко")
else: 
    print("Не круто")