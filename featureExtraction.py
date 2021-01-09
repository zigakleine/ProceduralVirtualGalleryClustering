from tensorflow.keras.applications import vgg16
from tensorflow import keras


class FeatureExtraction:

    def __init__(self):
        self.IMG_SIZE = 224
        model_base = vgg16.VGG16(weights='imagenet', include_top=True, input_shape=(self.IMG_SIZE, self.IMG_SIZE, 3))
        self.model = keras.Model(inputs=model_base.layers[0].input, outputs=model_base.layers[-2].output)
        self.model.summary()

    def extract_features(self, imgs):

        feature_vectors = []

        for img in imgs:
            img_expand = img.reshape(1, self.IMG_SIZE, self.IMG_SIZE, 3)
            res = self.model.predict(img_expand)
            feature_vectors.append(res[0])

        return feature_vectors
