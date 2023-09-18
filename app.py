# v0.2

from flask import Flask , request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.now()
    return f"hello Will , the time now is {now}\n"


app.run ( "0.0.0.0" , 8080  )
