from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/webhook", methods=['POST'])
def webhook():
    # Handle incoming messages from WhatsApp
    incoming_message = request.values.get('Body', '').lower()
    
    # Process the message and generate a response
    response_message = process_message(incoming_message)
    
    # Send a WhatsApp message using the provided code snippet
    send_whatsapp_message(response_message)
    
    return "OK"

def process_message(message):
    # Implement your chatbot logic here based on the user's message
    if "hello" in message:
        return "Hello! How can I assist you today?"
    else:
        return "I'm sorry, I don't understand that request."

def send_whatsapp_message(message):
    # The provided code for sending a WhatsApp message using requests
    url = "https://graph.facebook.com/v17.0/119010511301211/messages"

    headers = {
        "Authorization": "Bearer EAANZC1vXyEJYBO11lYkcdyBGYgR48rZBAWVp71V2uEBpQFAoQIByvb1QyVZBrPajZAgS4lrxWF2J2iedsUaW5exRsI1jhXqcuGTrUzuZBH9KrxcJhvjSogvJ0ZBbhZCW081dmPSj0T2rihGj8mWbq0tMDoJISA5KPYns8OZABrpzZCoGWiZABUPsniM23Gxff1q3gCPJBF0Wc1b4DkFcZBy12U2rwYhZANGSk9C4obcZD",
        "Content-Type": "application/json"
    }

    data = {
        "messaging_product": "whatsapp",
        "to": "255699722149",
        "type": "template",
        "template": {
            "name": "hello user I got by the name Amina.",
            "language": {
                "code": "en_US"
            }
        }
    }

    response = requests.post(url, headers=headers, json=data)

    print(response.text)

if __name__ == "__main__":
    app.run(debug=True)
