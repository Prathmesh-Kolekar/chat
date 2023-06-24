import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/static/<path:path>')
def send_static(path):
    return app.send_static_file('static/' + path)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    message = request.json['message']
    print(message)
    # Define the API endpoint and payload
    api_endpoint = 'https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium'
    headers = {'Authorization': 'Bearer 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'}
    payload = {'inputs': message}

    # Make the API request
    response = requests.post(api_endpoint, headers=headers, json=payload)
    data = response.json()
    # print(data)
    # Get the chatbot reply from the API response
    reply = data['generated_text'].strip()
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run()
