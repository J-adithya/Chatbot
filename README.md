# NLP-Powered Chatbot
This project is intended to showcase my work done during my internship at the company Muonium.ai

# Introduction
This project is an NLP-powered chatbot built using Flask for the backend and HTML, CSS, and JavaScript for the frontend. The chatbot interface supports Markdown formatting, including bold and italics, and allows users to enter multiline messages using Shift + Enter.

![Screenshot 2024-08-21 182544](https://github.com/user-attachments/assets/b4e95e9a-66d7-4de6-8c5d-1328a3a54405)


# Table of Contents
- Features  
- Dependencies  
- Installation  
- Usage  
- Project Structure  
- License  

# Features
- Markdown formatting support (bold, italics, etc.)  
- Multiline message input using Shift + Enter  
- Real-time message sending with Enter  
- Typing indicators and loading animation  
- Light and dark theme toggle  
- Clear chat and download chat functionalities  

# Dependencies

**Backend:**  
Flask - A micro web framework for Python  
requests - A simple HTTP library for Python  

**Frontend:**  
Marked.js - A markdown parser and compiler

# Installation

1. **Clone the repository:**

```bash
git clone https://github.com/J-adithya/Chatbot.git
cd Chatbot
```

2. **Set up a virtual environment and install dependencies:**

```
python -m venv chatbot_venv
source chatbot_venv/bin/activate  # On Windows use `chatbot_venv\Scripts\activate`
pip install Flask requests
pip install -r requirements.txt
```

3. Run the Flask server:
```
python app.py
```


# LM Studio Installation and Model Setup

This project requires LM Studio to be installed on your local machine. LM Studio is used to run the Llama 8B Instruct model on a local server, which the chatbot interacts with. Follow the steps below to set up LM Studio:

**Download and Install LM Studio:**

Visit the LM Studio GitHub repository or the official website to download the latest version of LM Studio.

Follow the installation instructions for your operating system (Windows, macOS, Linux).
Load the Llama 8B Instruct Model: (Any model of your choice can also be used)

Once LM Studio is installed, launch the application.
Go to the Model Management section and download the "Llama 8B Instruct" model.
After downloading, load the model into the local server by following these steps:
Navigate to the Local Server section.
Select the "Llama 8B Instruct" model from the available models.
Start the server by clicking on the Start Server button.
Ensure that the server is running at http://localhost:1234/v1/chat/completions.

**Configure the Flask App:**

The Flask app in this project is configured to interact with the LM Studio server at http://localhost:1234/v1/chat/completions.
Ensure that the LM Studio server is running before you start the Flask server. 

This setup allows for custom fine tuning of the model's responses in the system prompt panel (Make sure to reload the model to affect changes).  

# User Experience and Design Mindmap
- To interact with the chatbot, simply type your message in the input box and press Enter.
- Use Shift + Enter to enter multiline messages.
- Toggle between light and dark themes using the theme toggle button.
- Clear the chat or download the conversation using the provided buttons.

# UI Features
- Modern Design: A clean and modern interface for a smooth user experience.
- Responsive Layout: Ensures compatibility across various devices and screen sizes.
- Instant Feedback: Provides immediate responses to user queries, enhancing engagement.


**Project Structure**

```
/Chatbot
│── /frontend
│   ├── index.html
│   ├── styles.css
│   ├── script.js
│── app.py
│── requirements.txt
│── README.md
```
Thank You for visiting this project, hope you like it.
