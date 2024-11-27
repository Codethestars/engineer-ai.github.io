from flask import Flask, render_template
import os

app = Flask(__name__, 
           template_folder='../templates',  # Point to templates directory
           static_folder='../static')       # Point to static directory

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()