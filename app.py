
from flask import Flask

app = Flask(__name__)


@app.route('/v1/hello-world-2')
def hello_world():
    return 'Hello World 2 !'


if __name__ == '__main__':
    app.run()