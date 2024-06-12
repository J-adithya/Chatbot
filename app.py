from flask import Flask, request, jsonify, send_from_directory
import requests
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__, static_folder='frontend', static_url_path='')

LM_STUDIO_URL = "http://localhost:1234/v1/chat/completions"
API_KEY = "lm-studio"

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data['message']
    logging.debug("Received message: %s", message)
    
    # Prepare the payload for the LM Studio API
    payload = {
        "model": "lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF",
        "messages": [
            {"role": "system", "content": "You are a professional assistant. Respond in a clear, concise, and polite manner."},
            {"role": "user", "content": message}
        ],
        "temperature": 0.7,
    }

    # Send the request to the LM Studio local server
    response = requests.post(LM_STUDIO_URL, json=payload, headers={"Authorization": f"Bearer {API_KEY}"})
    
    if response.status_code == 200:
        reply = response.json()['choices'][0]['message']['content']
        logging.debug("Generated reply: %s", reply)
        
        # Post-process the response
        reply = post_process_reply(reply)
        
        return jsonify({'reply': reply})
    else:
        logging.error("Error from LM Studio API: %s", response.text)
        return jsonify({'reply': "Error: Unable to generate a response"}), 500

def post_process_reply(reply):
    # Capitalize the first letter and add a period at the end if not present
    reply = reply.capitalize()
    if not reply.endswith('.'):
        reply += '.'
    
    # Additional professional filtering and formatting can be added here
    return reply

if __name__ == '__main__':
    app.run(debug=True)
