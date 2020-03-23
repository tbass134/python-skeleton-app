import os, sys, time, re
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

def main_menu():
    print("Menu")
    print("1. Edit .env values")
    print("2. Add .env variable")
    print("3. Exit")
    option = input("Enter an option: ")
    clear()
    return option

def edit_menu():
    global envfile
    print("Edit .env values\n")
    params = envfile.get_params()
    for index, param in enumerate(params):
        print("{} - {} = {}".format(index+1, param["name"], param["value"]))
    print("\nback - TO RETURN")
    option = input("Enter an option: ")
    clear()
    if option.isnumeric():
        index = int(option)
        if index in range(1,len(params)):
            name = params[index-1]['name']
            value = input("New value for {}: ".format(name))
            envfile.add_param(name, value)
            envfile.update()
    return option

def add_menu():
    global envfile
    print("Add .env variable")
    name = input("Enter the name (No spaces allowed): ")
    #If user put spaces replace them with _
    name = re.sub(r'[\s]+','_',name)
    value = input("Enter the value: ")
    envfile.add_param(name, value)
    envfile.update()
    print(".env file updated, returning to menu...")
    #option = input("Do you want to add another value y / n (n is default) ?")
    time.sleep(3)
    clear()
    return "back" #if option != "y" else ""

if not envfile.exists():
    envfile.add_param("NEXMO_API_KEY")
    envfile.add_param("NEXMO_API_SECRET")
    envfile.add_param("FROM_NUMBER")
    envfile.add_param("TO_NUMBER")
    envfile.create(ui=True)
    print(".env is ready")
else:
    print(".env file already exists")
opt = "0"

while opt != "3":
    opt = main_menu()
    if opt in ['1', '2']:
        sub_opt = "0"
        while sub_opt != "back":
            sub_opt = edit_menu() if opt == "1" else add_menu()

print("Bye")