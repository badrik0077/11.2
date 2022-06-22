from flask import Flask, request, render_template
import random

app = Flask(__name__)


@app.route('/')
@app.route('/')
def hello():
    is_blocked = random.choice([True, False])
    return render_template('hello.html', is_blocked=is_blocked)


app.run(debug=True)