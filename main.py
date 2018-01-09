from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template ('login.html')
    else: 
        return "Hello World!"

@app.route("/signup", methods=['POST', 'GET'])
def signed_up():
    return render_template('login1.html')

if __name__ == "__main__":
    app.secret_key = os.urandom(12) 
    app.run(debug=True, host='0.0.0.0', port=4000)