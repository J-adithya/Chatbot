# Chatbot-
This project is intended to showcase my work done during my internship at the company Muonium.ai

# Introduction-
Welcome to the MuonChat repository! MuonChat is a conversational AI chatbot designed to provide intelligent and engaging interactions with users. Leveraging the power of the Blenderbot model, a state-of-the-art conversational agent developed by Facebook AI, MuonChat is fine-tuned using a variety of datasets to enhance its knowledge and response capabilities in AI, programming, and general knowledge domains.

# Features-
1. Robust Dataset Integration
MuonChat is trained on a combination of datasets to ensure comprehensive coverage of various topics:

CodeSearchNet: Provides knowledge about programming, specifically Python, enhancing the bot's capability to handle coding-related queries.
AI2 ARC: Focuses on challenging science questions, strengthening the bot's ability to address complex queries.
SQuAD v2: A widely recognized QA dataset that improves the bot's general knowledge and comprehension abilities.

2. Advanced Model Fine-Tuning
Using the transformers library by Hugging Face, MuonChat fine-tunes the Blenderbot model to boost its conversational skills:

Efficient Tokenization and Mapping: Converts datasets into the model's required input format.
Mixed Precision Training: Utilizes fp16 mixed precision training for faster and more efficient model training.
Custom Training Parameters: Balanced training parameters to optimize performance and computational efficiency.

3. User-Friendly Web Interface
MuonChat provides a seamless user experience through a web interface built with Flask:

Main Interface (/): Serves the main user interface of the chatbot.
Chat Endpoint (/chat): Processes POST requests to handle user input and generate responses.

4. Professional Response Post-Processing
To ensure polished and professional interactions, MuonChat responses undergo post-processing:

Capitalization: The first letter of the response is capitalized.
Punctuation: Ensures the response ends with appropriate punctuation.

5. Easy Deployment
MuonChat is designed for straightforward deployment:

Model and Tokenizer Saving: Fine-tuned model and tokenizer are saved for easy loading and deployment.
Flask Integration: The Flask app can be run locally for development or deployed on a server for production use.

6. Interactive UI
MuonChat features an intuitive and interactive user interface:

Modern Design: A clean and modern interface for a smooth user experience.
Responsive Layout: Ensures compatibility across various devices and screen sizes.
Instant Feedback: Provides immediate responses to user queries, enhancing engagement.

