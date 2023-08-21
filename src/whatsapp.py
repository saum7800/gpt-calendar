
from flask import Flask, request
import requests
from twilio.rest import Client
import dotenv
import os

dotenv.load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

client = Client(account_sid, auth_token)
 
app = Flask(__name__)

def send_response(sender, message_body):
    response = client.messages.create(
        body="Thanks for saying: " + message_body,
        from_='whatsapp:+14155238886',  # Your Twilio WhatsApp number
        to=sender  # Sender's WhatsApp number
    )
    return response


@app.route("/", methods=["POST"])
def bot():
 
    # user input
    sender, user_msg = request.values.get('From', ''), request.values.get('Body', '')

    # send response
    response = send_response(sender, user_msg)
    print(f"response: {response.sid}")
    return(str(response))
 
 
if __name__ == "__main__":
    app.run()