from flask import Flask

app = Flask(__name__)

# This is a Hello World Code!!
@app.route('/')
def hello_world():
    return 'Hello, Payppy! :)'

@app.route('/hello')
def hello_world():
    return 'Hello'


# initiating the program

