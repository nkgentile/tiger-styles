import os
import logging
import uuid
from flask import Flask, request, render_template, jsonify, redirect, url_for
from random import *
from flask_cors import CORS
from werkzeug import secure_filename
import requests
import json
from tools.config import UPLOAD_FOLDER
from tools.storage_utils import StorageUtils
from flask_socketio import SocketIO, emit
from tools.config import UPLOAD_FOLDER
from xform.tranImage import XForm

app = Flask(__name__,
            static_folder="./dist/static",
            template_folder="./dist")

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
su = StorageUtils()
ALLOWED_EXTENSIONS = set(['png', 'ico', 'jpg', 'jpeg', 'gif'])

socketio = SocketIO(app)
@socketio.on('upload', namespace='/style')
def image_upload(submission):
    if (submission[ 'content' ]):
        # image = Image.frombytes('RGB', (128,128), file, 'jpg')
        # submission['content'].save('image.test.jpg')
        #TODO put this in try catch block and feature to upload / download file from S3
        fileName = submission[ 'id' ] + "_input.jpg"
        fileWPath = os.path.join(UPLOAD_FOLDER,fileName )
        f = open(fileWPath, 'wb')
        f.write(submission['content'])
        f.close()
        print("file uploaded as {} and saved locally".format(fileWPath))
        print(submission[ 'style' ])
        xf = XForm()
        status, outputImage, msg = xf.process_image(fileWPath, 
                            submission['style'], False)
        if status == True:
            #convert the output imafge into a binary blob
            f = open (outputImage, 'rb')
            styledImageBlob = f.read()
            emit('success', styledImageBlob, namespace='/style')
        else:
            emit("error", msg, namespace ='/style')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == "__main__":
    app.run(debug=True)
