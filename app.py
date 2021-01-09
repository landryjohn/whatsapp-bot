import requests 
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    """
    endpoint to list to the twilio API webhook, each time an icoming 
    from an user is received by twilio, this endpoint will be invoke
    """
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    resp_msg = resp.message()
    responded = False 

    if "quote" in incoming_msg :
        try:
            r = get_quote() 
            quote = f"{r['content']} - {r['author']}" 
        except Exception :
            quote = "Je ne peut pas trouver de citation pour le moment..."
        resp_msg.body(quote)
        responded = True 
    
    if "cat" in incoming_msg :
        resp_msg.media("https://cataas.com/cat")
        responded = True 

    if not responded :
        resp_msg.body("Le bot ne comprend pas ça...") 
        
    return str(resp)

def get_quote() -> str:
    response = requests.get("https://api.quotable.io/random")
    if response.status_code == 200 :
        return response.json()
    else : 
        raise Exception()
    
if __name__ == "__main__":
    app.run()