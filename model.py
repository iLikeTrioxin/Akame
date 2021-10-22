import tensorflow as tf
import os
import ass

asciiSigns = [chr(i) for i in range(128)]

idsFromChars = tf.keras.layers.experimental.preprocessing.StringLookup(
    vocabulary=asciiSigns,
    mask_token=None
)

charsFromIds = tf.keras.layers.experimental.preprocessing.StringLookup(
    vocabulary=idsFromChars.get_vocabulary(),
    invert=True,
    mask_token=None
)


def idsFromTexts(texts: list) -> list:
    return idsFromChars(tf.strings.unicode_split(texts, input_encoding='UTF-8'))


def textsFromIds(ids: list) -> list:
    return tf.strings.reduce_join(charsFromIds(ids), axis=-1)


subtitlesDir = "/root/Akame/subs"

dials = []

for sub in os.listdir(subtitlesDir):
    with open(f"{subtitlesDir}/{sub}", encoding='utf-8-sig') as file:
        for event in ass.parse(file).events:
            dials
            if event.name is "Akame" and previousEvent is not None:
                dials.append([previousEvent, event.text])
            previousEvent = event.text


class AkameText(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim, rnn_units):
        super().__init__(self)
        self.embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim)
        self.gru = tf.keras.layers.GRU(rnn_units,
                                       return_sequences=True,
                                       return_state=True)
        self.dense = tf.keras.layers.Dense(vocab_size)

    def call(self, inputs, states=None, return_state=False, training=False):
        x = inputs
        x = self.embedding(x, training=training)

        if states is None:
            states = self.gru.get_initial_state(x)

        x, states = self.gru(x, initial_state=states, training=training)
        x = self.dense(x, training=training)

        if return_state:
            return x, states
        else:
            return x
