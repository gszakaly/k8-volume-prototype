import os
import uuid
from flask import Flask

OUTPUT_DIR = '/mnt/output'
STORAGE_DIR = '/mnt/storage'

app = Flask(__name__)

@app.route('/')
def process():
    file_name = str(uuid.uuid4()) + '.txt'
    with open(os.path.join(OUTPUT_DIR, file_name), 'w') as f:
        f.write('Start\n')
    with open(os.path.join(STORAGE_DIR, file_name), 'w') as f:
        f.write('Start\n')
    
    response = '<h1>Files</h1>\n'

    files = list(os.scandir(STORAGE_DIR))
    files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
    for file in files:
        response += f'<h3>{file.path}</h3>\n'
        with open(file.path, 'r') as file:
            for line in file:
                response += f'<div>{line}</div>\n'


    return response

