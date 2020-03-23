import os, sys, time, re
from os.path import dirname
import nexmo

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

option = 0

if envfile.exists():
    while option != "3":
        print("Nexmo Ops")
        print("1. Check credentials")
        print("2. Send a SMS")
        print("3. Exit")
        option = input("Enter your option: ")
        if option == "1":
            clear()
            print("Testing credentials....")
            time.sleep(3)
            #print(os.environ.get('NEXMO_API_KEY') + " " + os.environ.get('NEXMO_API_SECRET') + " " + os.environ.get('NEXMO_APPLICATION_ID') + " " + os.environ.get('NEXMO_PRIVATE_KEY_NAME'))
            try:
                client = nexmo.Client(
                    key = os.environ.get('NEXMO_API_KEY'),
                    secret = os.environ.get('NEXMO_API_SECRET')
                )
                result = client.get_balance()
                print("Valid Key and secret credentials.")
                if os.environ.get('NEXMO_APPLICATION_ID') is not None:
                    private_key = envfile = env(directory + '/' + os.environ.get('NEXMO_PRIVATE_KEY_NAME'))
                    client = nexmo.Client(
                        application_id = os.environ.get('NEXMO_APPLICATION_ID'),
                        private_key = os.environ.get('NEXMO_PRIVATE_KEY_NAME')
                    )
                    print("Valid voice credentials")
            except nexmo.errors.AuthenticationError:
                #print(sys.exc_info()[0].__dict__)
                print("Authentication Error: invalid credentials")
            except FileNotFoundError:
                print("Invalid Voice credentials: Your private key file path is invalid. Use absolute path")
            except:
                print(sys.exc_info()[0])
            finally:
                time.sleep(3)
                clear()
        elif option == "2":
            try:
                clear()
                print("Send test sms")
                to = input("Enter the destination number: ")
                #clean the to param using regexp
                to = re.sub(r'[\(\)\-\+]*','',to)
                #print(to)
                client = nexmo.Client(
                    key = os.environ.get('NEXMO_API_KEY'),
                    secret = os.environ.get('NEXMO_API_SECRET')
                )
                result = client.send_message(
                    {
                        "from": os.environ.get("NEXMO_NUMBER"),
                        "to": to,
                        "text": "A text message sent using the Nexmo SMS API"
                    }
                )
            except:
                print(sys.exc_info()[0])
                print("Error when trying to send a sms")
            finally:
                time.sleep(3)
                clear()
else:
    print("I need the .env file. Use the helper/init.app.py to create it")