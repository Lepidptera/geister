from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Setting

status = model.Status
othello = model.Othello

@app.route('/',methods=['GET','POST'])
def index():



if __name__ == '__main__':
    app.run(port=5000, threaded=True)