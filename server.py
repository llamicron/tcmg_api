import hashlib
import json

from flask import Flask

app = Flask(__name__)

@app.route('/md5/<string>')
def md5(string):
    return json.dumps({
        'input': string,
        'output': hashlib.md5(bytes(string, 'utf-8')).hexdigest()
    })

@app.route('/factorial/<number>')
def factorial(number):
    num = int(number)

    if num < 0:
        output = 'Error: integer needs to be positive'
    else:
        output = 1
        for i in range(1, num + 1):
            output = i * output

    return json.dumps({
        'input': number,
        'output': output
    })
