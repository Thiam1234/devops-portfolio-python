from flask import Flask, render_template
import os
import socket
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',
                         build_number=os.environ.get('BUILD_NUMBER', 'local'),
                         hostname=socket.gethostname(),
                         date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
