import base64
import glob
import io

import numpy as np
from flask import Flask, jsonify, request
from PIL import Image

from similar import findSimilarity

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['JSON_SORT_KEYS'] = False
app.config['ENV'] = 'development'

@app.route('/api/similarity/getImageList', methods=['GET'])
def getImageList():
    print('[INFO]--[getImageList]--[FUNCTION]')
    imageList = []
    for fileName in glob.glob('imageList/*.jpg'):
        with open(fileName, 'rb') as imageFile:
            imageInfo = fileName.split('\\')[1].split('.')
            imageName = imageInfo[0]
            imagePrefix = imageInfo[1]
            imageBase64 = base64.b64encode(imageFile.read()).decode()
            dict = {'imageName': imageName, 'imagePrefix': imagePrefix,
                    'imageBase64': str(imageBase64)}
            imageList.append(dict)
    return jsonify(imageList)

@app.route('/api/similarity/getImageBase64FromQR', methods=['POST'])
def getImageBase64FromQR():
    print('[INFO]--[getImageBase64FromQR]--[FUNCTION]')
    imageName = request.form['imageName']
    with open('imageList/'+imageName, 'rb') as imageFile:
        imageBase64 = base64.b64encode(imageFile.read())
    imageBase64 = imageBase64.decode()
    return jsonify({'imageBase64':imageBase64})

@app.route('/api/similarity/getSimilaritiyRateFromImage', methods=['POST'])
def getSimilaritiyRateFromImage():
    print('[INFO]--[getSimilaritiyRateFromImage]--[FUNCTION]')
    imageName = request.form['compareImageName']
    imageString = request.form['imageBase64']

    imageData = base64.b64decode(str(imageString))
    compareImage = Image.open(io.BytesIO(imageData))

    similarityRate = findSimilarity(imageName, np.array(compareImage), 0)
    similarityRate = str(similarityRate*100)
    return jsonify({'similarityRate':similarityRate})

@app.route('/api/test/getTest', methods=['GET'])
def getTest():
    print('[INFO]--[getTest]--[FUNCTION]')
    return jsonify('Test Successful')

@app.route('/api/test/getTestJenkins', methods=['GET'])
def getTestJenkins():
    print('[INFO]--[getTest]--[FUNCTION]')
    return jsonify('Test Successful for Jenkins')

@app.route('/', methods=['GET'])
def home():
    print('[INFO]--[home]--[FUNCTION]')
    homePage = '''
        <html>
    <head>
        <style>
            h1 {text-align: center;}
        </style>
    </head>
    <body>
        <h1>WELCOME TO THE SANAMUZE WEB API</h1>
    </body>
    </html>
    '''
    return homePage

@app.route('/favicon.ico')
def favicon():
    return 'None'
    
if __name__ == '__main__':
    app.run()
