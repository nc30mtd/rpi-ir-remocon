from flask import Flask, request, render_template
from datetime import datetime
import json
import threading
from queue import Queue
import subprocess
import glob
# from irrp_module import IRRP


GPIO=23
PORT = 5000
CODEFILE='codes'
app = Flask(__name__, static_folder='./templates/images')

task_queue = Queue()
result_queue = Queue()

@app.route('/')
def index():
    data =[]
    return render_template('index.html', data=data) # templatesフォルダ内のindex.htmlを表示する

# @app.route('/send')
# def send():
#     value = 'None'
#     if request.method == 'POST':
#         data = json.loads(request.data) 
#         value = data['method']
        
#         ir = IRRP(file=CODEFILE, no_confirm=True)
#         ir.Playback(GPIO=GPIO, ID=value)
#         ir.stop()
#     return str(value)

def mearge_codes():
    ret = {}
    codelist = glob.glob('./codes/*')
    for codefile in codelist:
        with open(codefile) as f:
            text = f.read()
            item = json.loads(text)
            print(item)
            ret.update(item)
    jsontext = json.dumps(ret)
    with open('code.json', 'w', encoding='utf-8') as f:
        f.write(jsontext)
    
if __name__ == '__main__':
    mearge_codes()
    app.run(port=PORT, host='0.0.0.0', debug=True, threaded=True)