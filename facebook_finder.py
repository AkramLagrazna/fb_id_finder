import requests
import json
import webbrowser

print("-------------------------------------")
print("Welcome to Facebook ID Profile Finder")
print("-------------------------------------")


userid = raw_input("Please enter the Facebook ID   ")
user_have_token = raw_input("Do you have an access token? y/n  ")
n = str('n')
y = str('y')
if user_have_token is n:
    facebook_request = requests.get('https://graph.facebook.com/'+str(userid)+"?access_token=EAACEdEose0cBALtdu49SgChQjKnAen22FZB38tvvAAJpNOjNv82xRlVTpZAPASZBBVmZAGTVZAnZAZCuPQQ7ZB3517eS7XlycuWRkZBodRn72SL9gZCvxElIWZBq4COCnwjwUR1jLaobU0q9J7g60En0kia0Mc7k2ts7hWXwx5tkZCmeMs6MKgxNasNewYZAdcblMAhYZD")

    print("Connecting...")
    if facebook_request.status_code is 200:
        print("Connection Established")
        json = facebook_request.json()
        print(json)
        print("..")
        see_profile = raw_input("Do you want to see the facebook profile on browser?")
        if see_profile is n:
            print("Okay, bye bye")
        elif see_profile is y:
            print("Okay, opening now the profile!")
            print("See you!")
            webbrowser.open("https://facebook.com/profile.php?id="+str(userid))
    else:
        print("Error connecting..")
        print("Program is exiting..")

elif user_have_token is y:
    access_token = raw_input("Please enter your access token.   ")
    facebook_request = requests.get('https://graph.facebook.com/'+str(userid)+"?access_token="+str(access_token))

    print("Connecting...")
    if facebook_request.status_code is 200:
        print("Connection Established")
        json = facebook_request.json()
        print(json)
        print("..")
        see_profile = raw_input("Do you want to see the facebook profile on browser?")
        if see_profile is n:
            print("Okay, bye bye")
        elif see_profile is y:
            print("Okay, opening now the profile!")
            print("See you!")
            webbrowser.open("https://facebook.com/profile.php?id="+str(userid))
        
    else:
        print("Error connecting..")
        print("Program is exiting..")
        
else:
    print("Okay byee")
    
