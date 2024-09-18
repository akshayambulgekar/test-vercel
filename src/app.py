from flask import Flask, render_template, jsonify,request

app = Flask(__name__)

# This is a Hello World Code!!
@app.route('/')
def hello_world():
    return 'Hello, Payppy! :)'

@app.route('/hello')
def hello():
    return 'Hello'

@app.route('/name',methods=['GET'])
def name():
    name = float(request.args.get('name'))
    return 'Hello' + name


# initiating the program

