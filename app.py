from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return f'Hello Vinay here!\n'
