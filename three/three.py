import os
import uuid
from flask import Flask

INPUT_DIR = '/mnt/input'

app = Flask(__name__)

@app.route('/')
def process():
    response = '<h1>Files</h1>\n'

    files = list(os.scandir(INPUT_DIR))
    files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
    for file in files:
        response += f'<h3>{file.path}</h3>\n'
        with open(file.path, 'r') as file:
            for line in file:
                response += f'<div>{line}</div>\n'


    return response

