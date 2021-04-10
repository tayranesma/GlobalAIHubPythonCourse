# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 22:22:31 2021

@author: LENOVO
Homework-3
"""
#%%
"""
User login application:
    get username and password values from the user.
    check the values is an if statemend and tell the user if they were succesful
"""
    
username = "Esma"
password = "123456"

get_username = input("Please insert an username: ")
get_password = input("Please insert a password: ")

if (username != get_username and password == get_password):
    print("Wrong username, please try again!")
elif (username == get_username and password != get_password):
    print("Wrong password, please try again!")
elif (username != get_username and password != get_password):
    print("Both username and password are wrong, please try again!")
else:
    print("Congrats! :)")
#%%
"""
   Extra: try building the same user login application but this time use a dictionary. 
"""
login = {username : "Esma", password : "123456"}

get_username = input("Please insert an username: ")
get_password = input("Please insert a password: ")

if (login[username] != get_username and login[password] == get_password):
    print("Wrong username, please try again!")
elif (login[username] == get_username and login[password] != get_password):
    print("Wrong password, please try again!")
elif (login[username] != get_username and login[password] != get_password):
    print("Both username and password are wrong, please try again!")
else:
    print("Congrats! :)")


        
        

