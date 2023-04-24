from flask import Flask, request
import base64
import uuid
from waitress import serve

app = Flask(__name__)


@app.route("/")
def hello_world():
    print('this is dumb')
    return "Hello, World!!"


@app.route("/hi", methods=['POST'])
def hello():
    data = request.get_json()
    print('test1')
    print(data)
    return "<p>Hello, World!@@!</p>"


@app.route('/predict', methods=['POST'])
def predict():
    filename = uuid.uuid4()
    photo_encoded = request.get_json()['photo']
    photo = base64.b64decode(photo_encoded)

    with open(f'images/{filename}.jpg','wb') as f:
        f.write(photo)
    # image = 

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8080)