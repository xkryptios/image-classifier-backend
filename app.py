import tensorflow as tf
from transformers import AutoImageProcessor ,TFAutoModelForImageClassification
from PIL import Image
# import requests
# from tensorflow import keras
# from keras.preprocessing.image import ImageDataGenerator
from werkzeug.utils import secure_filename
from flask import Flask, request
import base64
import uuid
from waitress import serve

app = Flask(__name__)

img = Image.open('./images/test.jpeg')
image_processor = AutoImageProcessor.from_pretrained("google/vit-base-patch16-224")
inputs = image_processor(img, return_tensors="tf")

model = TFAutoModelForImageClassification.from_pretrained("google/vit-base-patch16-224")

@app.route("/")
def hello_world():
    print('this is dumb')
    return "Hello, World!!!"


@app.route('/classify', methods=['POST'])
def classify():
    filename = uuid.uuid4()
    file = request.files['image']
    file.save(f'images/{filename}.jpg')
    print('File uploaded successfully')
    print('Initialising classification...')

    logits = model(**inputs).logits
    predicted_class_id = int(tf.math.argmax(logits, axis=-1)[0])
    result = model.config.id2label[predicted_class_id]
    print('Classification Result:',result)
    return result

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8080)