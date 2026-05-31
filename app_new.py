import json
import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from google import genai

load_dotenv()

test = os.environ.get('TEST', 'brak zmiennej')
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', 'brak zmiennej')

client = genai.Client()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    history = []
    if request.method == 'POST':
        history = json.loads(request.form['history'])
        prompt = request.form['prompt']
        history.append({"role": "user", "parts": [{"text": prompt}]})
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=history
        )
        history.append({"role": "model", "parts": [{"text": response.text}]})

    return render_template('index.html',
                           history=history, history_json=json.dumps(history))


if __name__ == '__main__':
    app.run(debug=True)