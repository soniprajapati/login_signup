
import json
from pickle import TRUE

print("WELLCOM TO INSTAGRAM")

def log_in():
    data={}
    while TRUE:
        login=input("login/sign_up and enter exit:")
        if login=="signup":
            name2=input("enter your name:")
            hobby=input("enter your hobby:")
            education=input("enter your education:")
            link=input("want to link with your facebook!:")
            if link=="yes":
                print("linked")
        
            password2=int(input("creat your password:"))
            confirm=int(input("enter to confirm:"))
            if password2!=confirm:
                print("enter the correct password to confirm!")
                confirm=int(input("enter to confirm:"))
            data.update({name2:password2})
            f=open("login.json","w")
            json.dump(data,f,indent=4)
            f.close()
            print(data)

        elif login=="exit":
            break

        elif login=="login":
            name=input("enter your name:")
            password=int(input("enter your password:"))
            if password in data:
                print("hello!",name,"thank you for login")
                print("this is your profile")
                print(hobby)
                print(education)
            elif password not in data:
                print("please enter the correct password")
                password=int(input("enter your password:"))
            

log_in()
        