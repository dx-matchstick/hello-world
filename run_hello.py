from flask import Flask
app = Flask(__name__)


@app.route('/<name>', methods=['GET'])
def hello_world(name):
    return "Hello, {}!".format(name)


if __name__ == "__main__":
    app.run(host = '18.191.194.20',port=8000)
# github test
