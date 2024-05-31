
from flask import Flask, request, jsonify
from flask_ngrok import run_with_ngrok
from transformers import pipeline

app = Flask(__name__)
run_with_ngrok(app)

# Hugging Face의 대화 모델 로드
chatbot = pipeline('conversational', model='facebook/blenderbot-400M-distill')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    response = chatbot(user_input)
    return jsonify(response)

if __name__ == '__main__':
    app.run()
