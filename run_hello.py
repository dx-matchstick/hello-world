from flask import Flask
app = Flask(__name__)


@app.route('/<name>', methods=['GET'])
def hello_world(name):
    return "Hello, {}!".format(name)


if __name__ == "__main__":
    app.run(host='65.88.88.177', port=5000)
# github test
