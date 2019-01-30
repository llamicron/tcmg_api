import hashlib

from flask import Flask

app = Flask(__name__)


@app.route('/md5/<string>')
def md5(string):
    return hashlib.md5(bytes(string, 'utf-8')).hexdigest()

