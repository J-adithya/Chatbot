from flask import Flask, request, jsonify, send_from_directory
from transformers import BlenderbotForConditionalGeneration, BlenderbotTokenizer

app = Flask(__name__, static_folder='frontend', static_url_path='')

# Load the tokenizer and fine-tuned model
tokenizer = BlenderbotTokenizer.from_pretrained("./chatbot_model")
model = BlenderbotForConditionalGeneration.from_pretrained("./chatbot_model")

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data['message']
    inputs = tokenizer([message], return_tensors="pt")
    reply_ids = model.generate(**inputs, max_length=100, num_return_sequences=1, temperature=0.9)
    reply = tokenizer.decode(reply_ids[0], skip_special_tokens=True)
    
    # Post-process the response
    reply = post_process_reply(reply)
    
    return jsonify({'reply': reply})

def post_process_reply(reply):
    # Example post-processing: Capitalize the first letter and add a period at the end if not present
    reply = reply.capitalize()
    if not reply.endswith('.'):
        reply += '.'
    
    # Additional professional filtering and formatting can be added here
    return reply

if __name__ == '__main__':
    app.run(debug=True)
