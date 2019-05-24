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
#from xform.tranImage import XForm

app = Flask(__name__,
            static_folder="./dist/static",
            template_folder="./dist")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
su = StorageUtils()
ALLOWED_EXTENSIONS = set(['png', 'ico', 'jpg', 'jpeg', 'gif'])


@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/api/dwim', methods=['GET', 'POST'])
def postFiles():
    # response_object = {'status': 'success'}
    if request.method == 'POST':
        photo = request.files['photoFile']
        print(photo.filename)
        #imagefile = request.values.get('photoFile')
        styleID = request.values.get('style')
        print(styleID)
        userID = None

        if (styleID != None) and \
                (photo.filename != None and len(photo.filename) > 2):
            userID = uuid.uuid1().hex
            if allowed_file(photo.filename):
                filename = secure_filename(photo.filename)
                fileWPath = os.path.join(UPLOAD_FOLDER, filename)
                photo.save(fileWPath)
                print(fileWPath)
                objName = userID + ".photo"
                print(objName)
                ''' status, msg = su.fileUpload(fileWPath, objName)
                if status == False:
                    return("failed uploading file to S3") '''  # Not doing anything with s3 yet
                # logging.info("fileUpload - {}".format(msg))
                logging.info("fileUpload ok - no s3 yet")
                os.remove(fileWPath)
            else:
                logging.info("File {} not acceptable".format(photo.filename))
        else:
            return redirect("/")

    messages = json.dumps({"userID": userID, "styleID": styleID})

    response = app.response_class(
        response=json.dumps(styleID),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == "__main__":
    app.run(debug=True)
