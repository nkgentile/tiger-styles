import os
import logging
import requests
import json

from flask import Flask, request, render_template, jsonify, redirect, url_for
from flask_cors import CORS
from flask_socketio import SocketIO, emit
from werkzeug import secure_filename

from tools.config import UPLOAD_FOLDER, CONTENT_FOLDER, STYLED_FOLDER
# from tools.storage_utils import StorageUtils

from xform.tranImage import XForm

# Flask
app = Flask(__name__,
            static_folder="./frontend/dist/static",
            template_folder="./frontend/dist")

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# su = StorageUtils()
ALLOWED_EXTENSIONS = set(['png', 'ico', 'jpg', 'jpeg', 'gif'])

# CORS Middleware
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'

# Socket.io Middleware
socketio = SocketIO(app)


@socketio.on('upload', namespace='/style')
def image_upload(clientId, styleId, contentImage):
    if (contentImage):
        # TODO put this in try catch block and feature to upload / download file from S3
        fileName = "{}.jpg".format(clientId)
        fileWPath = os.path.join(CONTENT_FOLDER, fileName)

        f = open(fileWPath, 'wb')
        f.write(contentImage)
        f.close()

        print("file uploaded as {} and saved locally".format(fileWPath))
        print(styleId)

        xf = XForm()
        status, outputImage, msg = xf.process_image(fileWPath,
                                                    styleId, False)
        if status == True:
            # convert the output image into a binary blob
            f = open(outputImage, 'rb')
            styledImageBlob = f.read()
            print(outputImage)
            emit('success', styledImageBlob, namespace='/style')
        else:
            emit("error", msg, namespace='/style')


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
