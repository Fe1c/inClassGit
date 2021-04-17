import random 

def password(n):
    password_chars = 'abcdefghijklmnopqrstuvwxyz123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%'
    password_p = ''
    for i in range(n):
        password_p += random.choice(password_chars)
    print(password_p)

password(7)