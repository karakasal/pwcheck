import re
import getpass

pattern = re.compile(r"[A-Za-z0-9$%#@]{7,}\d$")

while True:
    print('''
* At least 8 letters long
* Last letter is a number\n''')
    
    password = getpass.getpass("What is your new password ")
    check = pattern.fullmatch(password)
    if check == None:
        print("\n-----Incorrect password-----")
        continue
    
    password_confirmation = getpass.getpass("Please confirm you password ")
    if password == password_confirmation:
        print("\n-----Password has been updated-----")
        break
    else:
        print("\n-----Incorrect password-----")
        continue