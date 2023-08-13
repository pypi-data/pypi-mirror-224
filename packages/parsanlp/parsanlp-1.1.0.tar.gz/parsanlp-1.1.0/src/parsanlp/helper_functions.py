import tensorflow as tf
import datetime


def create_tensorboard_callback(log_dir, name):
    path = log_dir + "/" + name + "/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    return tf.keras.callbacks.TensorBoard(path)


import zipfile


def unzip_data(filename):
    zip_ref = zipfile.ZipFile(filename, "r")
    zip_ref.extractall()
    zip_ref.close()
