import os, sys, time
from os.path import dirname

#clear for linux
clear = lambda: os.system('clear')

#verify if user execute this script from test directory
if "helpers" not in os.path.abspath('.'): 
    path = '.'
else:
    path = '..'

directory = os.path.abspath(path)
sys.path.insert(0, directory)

#import local modules
from lib.env import env

clear()
envfile = env(directory+"/.env")

if envfile.exists():
    print(".env file already exists. if you want re-init please delete .env file")
    sys.exit()
else:
    print("Nexmo Skeleton App")
    print("Genral data - SMS Support")
    key = input("Enter the Api key: ")
    secret = input("Enter the Api secret: ")
    number = input("Enter the Nexmo Number: ")
    to_number = input("Enter Destination Number for testings: ")
    envfile.add_param("NEXMO_API_KEY", key)
    envfile.add_param("NEXMO_API_SECRET", secret)
    envfile.add_param("NEXMO_NUMBER", number)
    envfile.add_param("TO_NUMBER", to_number)
    clear()
    voice_support = input("Do you want to add voice support y/n (n is default)?  ")
    if voice_support.lower() in ['yes','y']:
        clear()
        print("Voice support")
        application_id = input("Enter your Application Id: ")
        application_private_key = input("Enter your private key filename (put the file in the project directory). default: private.key ")
        application_private_key = 'private.key' if application_private_key == '' else application_private_key
        envfile.add_param("NEXMO_APPLICATION_ID", application_id)
        envfile.add_param("NEXMO_PRIVATE_KEY_NAME", application_private_key)
    envfile.create()
    clear()
    print(".env file created")

