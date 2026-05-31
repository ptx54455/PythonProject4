from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Witaj MERITO!</h1><p>Autor: Ula </p>'

if __name__ == '__main__':
    app.run(debug=True)