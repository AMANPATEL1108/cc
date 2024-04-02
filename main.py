# main.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello our Cloud Computing Project"

if __name__ == '__main__':
    app.run()
