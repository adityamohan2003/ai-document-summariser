# Flask web app for AI Document Summariser
# This connects our summariser tool to a webpage

from flask import Flask, render_template, request, jsonify
from groq import Groq
from dotenv import load_dotenv
import os

# Setting up Flask app
app = Flask(__name__)

# Setting up Groq client
# Get your free API key at console.groq.com
load_dotenv()
api_key = os.environ.get("GROQ_API_KEY")
client = Groq(api_key=api_key)

def summarise_text(text):
    # Sending the text to Groq API and asking it to summarise
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": f"""Please analyse the following text and provide:
                1. A concise summary (3-4 sentences)
                2. Five key points
                3. Main topics covered

                Text to analyse:
                {text}"""
            }
        ]
    )
    return response.choices[0].message.content

# Main page route
@app.route('/')
def home():
    return render_template('index.html')

# Summarise route — receives text and returns summary
@app.route('/summarise', methods=['POST'])
def summarise():
    data = request.get_json()
    text = data.get('text', '')

    if not text:
        return jsonify({'error': 'No text provided'})

    result = summarise_text(text)
    return jsonify({'result': result})

# Running the app
if __name__ == '__main__':
    app.run(debug=True)