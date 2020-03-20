from flask import Flask,url_for

app = Flask(__name__)


@app.route('/<a>')
def hello_world(a):
    return a

if __name__ == '__main__':
    app.run()
    with app.test_request_context():
        print(url_for('hello_world', _external=True, a=123))
