from flask import Flask 

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    """
    Webhook logic which list to the twilio API
    """