import nexmo, os, sys, requests
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


#For inbound sms

#Webhook for receipt/inbound sms status
@app.route('/webhooks/delivery', methods=['GET','POST'])
@app.route('/webhooks/inbound', methods=['GET','POST'])
def status():
    res = request.get_json()
    message = res["text"]
    from_number = res["msisdn"]
    prediction = get_prediction(message)
    try:
        result = client.send_message(
            {
                "from": os.environ.get("NEXMO_NUMBER"),
                "to": from_number,
                "text": prediction
            }
        )
    except:
        print("Unhandle error")
        return "Unhandled error", 200

    print(request.args or request.get_json())
    return "All OK.", 200

def get_prediction(message):
    url = os.getenv("API_GATEWAY_URL")+ "?message=" + message
    response = requests.request("GET", url)
    return response.json()["prediction"]
