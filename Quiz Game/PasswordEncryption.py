#Password Encryptor
from cryptography.fernet import Fernet

master_pwd = input("Enter the Master Password! \n")

    

def view():
    with open ("myfile.txt" , 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print(f"USERNAME: {user} | PASSWORD : {passw} ")

def add():
    name = input("ACCOUNT NAME: ")
    pwd = input("PASSWORD: ")
    with open ("myfile.txt","a") as f:
        f.write (name+" | "+pwd + "\n")

while True:
    mode = input("Do you wanna ADD a New Password or view the Existing Ones? (add/view) PRESS Q TO QUIT\n").lower()
    if mode == "q":
        break
    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("This is an Invalid Mode!")