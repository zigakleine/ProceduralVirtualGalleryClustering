from flask import Flask, request, jsonify, render_template
import base64
from PIL import Image
import io
import numpy as np
#import cv2
#opencv_python==4.4.0.44

from kmeansClustering import KMeansClustering

from featureExtraction import FeatureExtraction

app = Flask(__name__)
app.debug = False

@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html')


@app.route('/hello', methods=['GET'])
def hello():
    return jsonify("hello")


@app.route('/featureExtractionAndKmeans', methods=['POST'])
def extract_features_and_kmeans():
    request_body_json = request.json

    imgs = []
    #print(request_body_json)

    #print(len(request_body["images"]))
    IMG_SIZE = 224

    for image_64 in request_body_json["images"]:
        #print(image_64)
        base64_decoded = base64.b64decode(image_64)
        image = Image.open(io.BytesIO(base64_decoded))
        image_np = np.array(image)
        # image_np = cv2.resize(image_np, (IMG_SIZE, IMG_SIZE), interpolation=cv2.INTER_LINEAR)
        image_np = image_np/255
        imgs.append(image_np)

    #print(imgs[0])

    feature_extractor = FeatureExtraction()
    kmeans = KMeansClustering()

    feature_vectors = feature_extractor.extract_features(imgs)

    cluster_labels = kmeans.perform_clustering(feature_vectors, 3)

    cluster_labels = cluster_labels.tolist()


    return jsonify(cluster_labels)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

