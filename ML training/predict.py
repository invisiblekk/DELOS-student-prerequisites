import tensorflow as tf
from PIL import Image
import numpy as np

from CNN import CNN


class Predict(object):
    def __init__(self):
        weight = tf.train.latest_checkpoint('./ckpt')
        self.cnn = CNN()
        self.cnn.model.load_weights(weight)

    def predict(self, image_path):
        img = Image.open(image_path).convert('L')
        img = np.reshape(img, (28, 28, 1)) / 255.
        x = np.array([1 - img])
        y = self.cnn.model.predict(x)
        print(image_path)
        print('The digit is: ', 'even' if np.argmax(y[0]) == 0 else 'odd')
        print('----------------------------------------')


if __name__ == "__main__":
    predict = Predict()
    predict.predict('./test_images/0.png')
    predict.predict('./test_images/1.png')
    predict.predict('./test_images/4.png')
