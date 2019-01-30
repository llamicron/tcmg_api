import hashlib
import json

from flask import Flask

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


@app.route('/md5/<string>')
def md5(string):
    return json.dumps({
        'input': string,
        'output': hashlib.md5(bytes(string, 'utf-8')).hexdigest()
    })

@app.route('/factorial/<number>')
def fact(number):
    num = int(number)

    if num < 0:
        output = 'Error: integer needs to be positive'
    else:
        output = factorial(num)

    return json.dumps({
        'input': number,
        'output': output
    })


@app.route('/fibonacci/<number>')
def fib(number):
    num = int(number)

    if num < 0:
        output = 'Error: integer needs to be positive'
    else:
        output = fibonacci(num)

    return json.dumps({
        'input': number,
        'output': output
    })
