from flask import Flask , request

app = Flask(__name__)

@app.route("/")
def index():
    return "hello world\n"


app.run ( "0.0.0.0" , 7777  )
