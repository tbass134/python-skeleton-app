from env import env

# This is just a demo
# Create the env file if it doesn't exist
envfile = env(".env")
if not envfile.exists():
    envfile.add_param("NAME", "gueast")
    envfile.add_param("WELCOME_MESSAGE")
    envfile.create()
# read environment vars when the env file exists
environment = envfile.get_env_vars()
print(environment["NAME"])

# Modify environment var inline
name = input("Enter the name: ")
envfile.set_param("NAME", name)
envfile.update()

environment = envfile.get_env_vars(reload=True)
print(environment["NAME"])
