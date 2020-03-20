import os, sys
from os.path import dirname

#verify if user execute this script from test directory
if "tests" not in os.path.abspath('.'):
    path = '.'
else:
    path = '..'

directory = os.path.abspath(path)
sys.path.insert(0, directory)

#import local modules
from lib.env import env

#This is just a demo
#Create the env file when not exist
envfile = env(directory+"/.env")
if not envfile.exists():
    name = input("Enter your name: ")
    envfile.add_param("NAME", name)
    welcome_message = input("Enter your welcome message: ")
    envfile.add_param("WELCOME_MESSAGE",welcome_message)
    envfile.create()
#read environment vars when exist
#print(environment["NAME"])

#Modify environment var inline
#name = input("Enter the name: ")
#envfile.set_param("NAME",name)
#envfile.update()

environment = envfile.get_env_vars(reload=True)
#print(environment["NAME"])
print("Hi {1}, {0}".format(environment["WELCOME_MESSAGE"], environment["NAME"]))