import hashlib
import json
import requests

from flask import Flask, Response

app = Flask(__name__)

def factorial(num):
    output = 1
    for i in range(1, num + 1):
        output = i * output
    return output

def fibonacci(num):
    seq = [0, 1, 1]

    while seq[-2] + seq[-1] <= num:
        seq.append(seq[-2] + seq[-1])

    return seq

def is_prime(num):
    prime = True
    if num <= 1:
        prime = False
    else:
        for i in range(2, num):
            if num % i == 0:
                prime = False
    return prime

def send(message):
    webhook = 'https://hooks.slack.com/services/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'
    data = {
        'text': message
    }

    response = requests.post(
        webhook, data=json.dumps(data),
        headers={'Content-Type': 'application/json'}
    )

    return True if response.status_code == 200 else False

def response(input, output, code):
    data = {
        'input': input,
        'output': output
    }
    return Response(json.dumps(data), status=code, mimetype='application/json')


# Routes
@app.route('/')
def index():
    return 'It works!'

@app.route('/md5/<string>')
def md5(string):
    output = hashlib.md5(bytes(string, 'utf-8')).hexdigest()
    return response(string, output, 200)

@app.route('/factorial/<number>')
def fact(number):
    try:
        num = int(number)
        if num < 0:
            output = 'Error: integer needs to be positive'
            return response(number, output, 400)
        else:
            output = factorial(num)
            return response(number, output, 200)
    except ValueError:
        output = "Error: that's not a number"
        return response(number, output, 400)

@app.route('/fibonacci/<number>')
def fib(number):
    try:
        num = int(number)
        if num < 0:
            output = 'Error: integer needs to be positive'
            return response(number, output, 400)
        else:
            output = fibonacci(num)
            return response(number, output, 200)
    except ValueError:
        output = "Error: that's not a number"
        return response(number, output, 400)

@app.route('/is-prime/<number>')
def prime(number):
    try:
        num = int(number)
        if num < 0:
            output = 'Error: integer needs to be positive'
            return response(number, output, 400)
        else:
            output = is_prime(num)
            return response(number, output, 200)
    except ValueError:
        output = "Error: that's not a number"
        return response(number, output, 400)

@app.route('/slack-alert/<string>')
def slack_alert(string):
    output = send(string)
    return response(string, output, 200)


if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0', port=5000)
