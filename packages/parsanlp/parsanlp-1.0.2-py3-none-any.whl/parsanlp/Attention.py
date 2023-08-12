import tensorflow as tf


class AttentionHead(tf.keras.layers.Layer):
    def __init__(self, dmodel):
        super(AttentionHead, self).__init__()
        self.dims = dmodel
        # q, k, v correspond to query, key, value.
        self.qw = tf.keras.layers.Dense(dmodel)
        self.kw = tf.keras.layers.Dense(dmodel)
        self.vw = tf.keras.layers.Dense(dmodel)

    def call(self, input):
        query = self.qw(input)
        key = self.kw(input)
        vals = self.vw(input)

        score = tf.matmul(query, key, transpose_b=True)
        scaled_score = score / tf.math.sqrt(tf.cast(self.dims, float))
        weights = tf.nn.softmax(scaled_score, axis=-1)
        return tf.matmul(weights, vals)


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
