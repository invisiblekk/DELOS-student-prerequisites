import tensorflow as tf
from tensorflow.keras import datasets
import numpy as np

from CNN import CNN


class DataSets(object):
    def __init__(self):
        (train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()
        train_images = train_images.reshape((60000, 28, 28, 1))
        test_images = test_images.reshape((10000, 28, 28, 1))
        train_images, test_images = train_images.astype("float") / 255., test_images.astype("float") / 255.
        train_labels, test_labels = train_labels % 2, test_labels % 2
        val_images = train_images[-10000:]
        val_labels = train_labels[-10000:]
        train_images = train_images[:-10000]
        train_labels = train_labels[:-10000]

        train_images_augmented = [image for image in train_images]
        train_labels_augmented = [image for image in train_labels]
        for image, label in zip(train_images, train_labels):
            train_images_augmented.append(np.rot90(image, 2))
            train_labels_augmented.append(label)
        shuffle_idx = np.random.permutation(len(train_images_augmented))
        train_images_augmented = np.array(train_images_augmented)[shuffle_idx]
        train_labels_augmented = np.array(train_labels_augmented)[shuffle_idx]

        self.train_images, self.train_labels = train_images_augmented, train_labels_augmented
        self.val_images, self.val_labels = val_images, val_labels
        self.test_images, self.test_labels = test_images, test_labels


class Train:
    def __init__(self):
        self.cnn = CNN()
        self.data = DataSets()

    def train(self):
        check_path = './ckpt/cp-{epoch:04d}.ckpt'
        save_model_cb = tf.keras.callbacks.ModelCheckpoint(check_path, save_weights_only=True, verbose=1, period=5)

        self.cnn.model.compile(optimizer="rmsprop",
                               loss="sparse_categorical_crossentropy",
                               metrics=["sparse_categorical_accuracy"])
        self.cnn.model.fit(self.data.train_images,
                           self.data.train_labels,
                           epochs=5,
                           batch_size=64,
                           validation_data=(self.data.val_images, self.data.val_labels),
                           callbacks=[save_model_cb])
        self.cnn.model.evaluate(self.data.test_images, self.data.test_labels)


if __name__ == "__main__":
    train = Train()
    train.train()
