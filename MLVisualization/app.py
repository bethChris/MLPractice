from flask import Flask, url_for, request, render_template
from markupsafe import escape


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



with app.test_request_context():
    print(url_for('index'))
    print(url_for('static', filename='style.css'))
