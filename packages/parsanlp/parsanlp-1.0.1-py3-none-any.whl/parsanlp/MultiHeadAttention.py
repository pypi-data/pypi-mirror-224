import tensorflow as tf
from parsanlp.Attention import AttentionHead


class MultiHeadAttention(tf.keras.layers.Layer):
    def __init__(self, h, dmodel):
        super(MultiHeadAttention, self).__init__()
        self.h = h
        self.dims = dmodel

        self.heads = [AttentionHead(dmodel) for _ in range(h)]

        self.linear = tf.keras.layers.Dense(self.dims)
        self.add = tf.keras.layers.Add()

    def call(self, input):
        res = tf.concat([head(input) for head in self.heads], -1)
        res = self.linear(res)
        res = self.add([res, input])
        return res
