"""
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential()

# Add an Embedding layer expecting input vocab of size 1000, and
# output embedding dimension of size 64.
model.add(layers.Embedding(input_dim=1000, output_dim=64))

# Add a LSTM layer with 128 internal units.
model.add(layers.LSTM(128))

# Add a Dense layer with 10 units.
model.add(layers.Dense(10))

model.summary()

model.compile(optimizer='sgd', loss='mse')
# This builds the model for the first time:
model.fit(x, y, batch_size=32, epochs=10)

"""

import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.text import Tokenizer, text_to_word_sequence, one_hot
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.losses import BinaryCrossentropy
from tensorflow.keras.optimizers import Adam
import os
import ass

subs = os.listdir('/root/Akame/subs')

dials = []

for sub in subs:
    with open(f"/root/Akame/subs/{sub}", encoding='utf-8-sig') as file:
        previousEvent = None

        for event in ass.parse(file).events:
            if event.name == "Akame" and previousEvent != None:
                dials.append([previousEvent, event.text])

            previousEvent = event.text

tok = Tokenizer(num_words=None, lower=True)

tok.fit_on_texts(np.array(dials).flatten())

x = []
y = []

for dial in dials:
    if len(dial) == 2:
        tmp = (tok.texts_to_sequences(dial))
        x.append(tmp[0])
        y.append(tmp[1])

x = np.array(pad_sequences(x))
y = np.array(pad_sequences(y))

x = x / len(tok.word_index)
y = y / len(tok.word_index)

print(x)
print(y)

model = keras.Sequential(
    [
        layers.Dense(17),
        layers.Dense(64),
        layers.Dense(96),
        layers.Dense(48),
        layers.Dense(17)
    ]
)

loss_function = BinaryCrossentropy()
optimizer     = Adam()

model.compile(optimizer=optimizer, loss=loss_function, metrics=['accuracy'])

model.summary()

# This builds the model for the first time:
model.fit(x, y, batch_size=128, epochs=64)

x = tok.texts_to_sequences(["Hi, Akame"])[0]
x = np.array([x, [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]])
x = pad_sequences(x)
x = x / len(tok.word_index)
x = model.predict(x) * len(tok.word_index)
x = x.astype(int)

vals = list(tok.word_index.values())
keys = list(tok.word_index.keys  ())

for i in x:
    for j in i:
        if j <= 0:
            continue
        print(keys[vals.index(j)], end=' ')
    print(' ')

model.save('my_model')