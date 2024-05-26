import random
import smtplib
import getpass

print("Welcome to random password Generator")
randomChar = "QWERTYUIOPASDFGHJKLZXCVBNMzxcvbnmasdfghjklqwertyuiop123456789!@#$%^&*())))))_+<>?:"
count = int(input("Enter the number of passwords to be generated: "))
length = int(input("Enter the length of the password: "))

print("Below are the passwords needed: ")

passwords = []

for x in range(count):
    pwd = ""
    for chars in range(length):
        pwd += random.choice(randomChar)
    passwords.append(pwd)
    print(pwd)

HOST = "smtp.gmail.com"
PORT = 587

From_Email = 'karuppaswamiks@gmail.com'
To_Email = 'kkswami.2208@gmail.com'
CC_Email = 'Karuppaswamiks@gmail.com'
Password = getpass.getpass("Enter Password: ")

smtp = smtplib.SMTP(HOST, PORT)
smtp.starttls()
smtp.login(From_Email, Password)

subject = "Password"
message = f"""Subject: {subject}\n\n
Hi name,\n
Below are the passwords for your reference:\n
{', '.join(passwords)}\n\n
Thank you!\n
Steve
"""

smtp.sendmail(From_Email, [To_Email, CC_Email], message)
smtp.quit()
