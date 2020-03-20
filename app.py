import nexmo, os, sys
from flask import Flask, request, jsonify
from dotenv import load_dotenv

app = Flask(__name__)

#this file contains the very basic skeleton to work with webhooks

#Create the nexmo client
load_dotenv('.env')
client = nexmo.Client(
    key = os.environ.get('NEXMO_API_KEY'),
    secret = os.environ.get('NEXMO_API_SECRET')
)

#Endpoint to check credentials
@app.route('/check-credentials', methods=['GET'])
def credentials():
    try:
        client.get_balance()
        return "Valid credentials", 200
    except nexmo.errors.AuthenticationError:
        return "Invalid credentials", 200
    except:
        print("Unhandle error")
        print(sys.exc_info()[0].__dict__)
        return "Unhandled error", 200

#Endpoint to send sms
@app.route('/send-sms', methods=['GET'])
def sms():
    try:
        result = client.send_message(
            {
                "from": os.environ.get("NEXMO_NUMBER"),
                "to": os.environ.get("TO_NUMBER"),
                "text": "A text message sent using the Nexmo SMS API"
            }
        )
        return "Server response: {}".format(result), 200
    except:
        print("Unhandle error")
        return "Unhandled error", 200

#For inbound sms

#Webhook for receipt/inbound sms status
@app.route('/webhooks/delivery', methods=['GET','POST'])
@app.route('/webhooks/inbound', methods=['GET','POST'])
def status():
    res = jsonify(request.json)
    print("Inbound SMS handler")
    print(request.args or request.get_json())
    return "All OK.", 200

#For calls

#Webhook for tracking an inbound call status
@app.route('/webhooks/event', methods=['GET','POST'])
def event():
    res = jsonify(request.json)
    print("Call Status Event handler")
    print(request.args or request.get_json())
    return "All OK.", 200

#Webhook for return NCCO for an inbound call
@app.route('/webhooks/answer', methods=['GET','POST'])
def answer():
    res = jsonify(request.json)
    print("Inbound Call handler")
    print(request.args or request.get_json())
    speech_text = "An speech ncco for nexmo"
    #In this example ncco is a speech text, but you can return custom NCCO according to your needs 
    return jsonify([
            {
                "action": "talk",
                "text": speech_text
            }
        ])

