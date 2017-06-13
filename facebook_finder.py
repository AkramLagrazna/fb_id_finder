import requests
import json
import webbrowser

print("-------------------------------------")
print("Welcome to Facebook ID Profile Finder")
print("-------------------------------------")
def exittt():
    exitttt = raw_input("You want to exit? y/n ")
    if exitttt is n:
        print("Perfect, staying here! ")
        print(".......................")
    else:
        print("Perfect see you, byeee!")
        print("+++++++++++++++++++++++")
        active = False

active = True
while active: 
    userid = raw_input("Please enter the Facebook ID   ")
    user_have_token = raw_input("Do you have an access token? y/n  ")
    n = str('n')
    y = str('y')
    if user_have_token is n:
        facebook_request = requests.get('https://graph.facebook.com/'+str(userid)+"?access_token=321713511595396|Yezd2aNvkEkOs9qYXGiQN-QHcKs")
    
        print("Connecting...")
        if facebook_request.status_code is 200:
            print("Connection Established")
            json = facebook_request.json()
            print("Name : "+str(json['name'])+"")
            print("Id   : "+str(json['id'])+"")
            print("+++++++++++++++++++++++++++")
            see_profile = raw_input("Do you want to see the facebook profile on browser? y/n ")
            if see_profile is n:
                print("Okay, bye bye")
            elif see_profile is y:
                print("Okay, opening now the profile!")
                webbrowser.open("https://facebook.com/profile.php?id="+str(userid))
                exittt()
        else:
            print("Error connecting..")
            exittt()
            
    
    elif user_have_token is y:
        access_token = raw_input("Please enter your access token.   ")
        facebook_request = requests.get('https://graph.facebook.com/'+str(userid)+"?access_token="+str(access_token))
    
        print("Connecting...")
        if facebook_request.status_code is 200:
            print("Connection Established")
            json = facebook_request.json()
            print("Name : "+str(json['name'])+"")
            print("Id   : "+str(json['id'])+"")
            print("+++++++++++++++++++++++++++")
            see_profile = raw_input("Do you want to see the facebook profile on browser? y/n ")
            if see_profile is n:
                print("Okay, bye bye")
            elif see_profile is y:
                print("Okay, opening now the profile!")
                webbrowser.open("https://facebook.com/profile.php?id="+str(userid))
                exittt()
        elif facebook_request.status_code is 404:
            print("ID doesn't exists!")
            exittt()
        
           
        else:
            print("Error connecting..")
            exittt()
        
    else:
        print("Okay byee")
    
