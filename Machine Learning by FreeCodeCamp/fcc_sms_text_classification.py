# -*- coding: utf-8 -*-
"""fcc_sms_text_classification.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/github/freeCodeCamp/boilerplate-neural-network-sms-text-classifier/blob/master/fcc_sms_text_classification.ipynb
"""

# import libraries
try:
  # %tensorflow_version only exists in Colab.
  !pip install tf-nightly
except Exception:
  pass
import tensorflow as tf
import pandas as pd
from tensorflow import keras
!pip install tensorflow-datasets
import tensorflow_datasets as tfds
import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)

# get data files
!wget https://cdn.freecodecamp.org/project-data/sms/train-data.tsv
!wget https://cdn.freecodecamp.org/project-data/sms/valid-data.tsv

train_file_path = "train-data.tsv"
test_file_path = "valid-data.tsv"

train_data = pd.read_csv(train_file_path, sep="\t", names=["label", "message"])
test_data = pd.read_csv(test_file_path, sep="\t", names=["label", "message"])

train_data['label'] = train_data['label'].map({'ham': 0, 'spam': 1})
test_data['label'] = test_data['label'].map({'ham': 0, 'spam': 1})

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

tokenizer = Tokenizer()
tokenizer.fit_on_texts(train_data['message'])

train_sequences = tokenizer.texts_to_sequences(train_data['message'])
test_sequences = tokenizer.texts_to_sequences(test_data['message'])

max_length = 20
X_train = pad_sequences(train_sequences, maxlen=max_length)
y_train = train_data['label'].values
X_test = pad_sequences(test_sequences, maxlen=max_length)

model = keras.Sequential([
    keras.layers.Embedding(input_dim=len(tokenizer.word_index) + 1, output_dim=16, input_length=max_length),
    keras.layers.GlobalAveragePooling1D(),
    keras.layers.Dense(16, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X_train, y_train, epochs=50, validation_split=0.2)

# function to predict messages based on model
# (should return list containing prediction and label, ex. [0.008318834938108921, 'ham'])
def predict_message(message):
    sequence = tokenizer.texts_to_sequences([message])
    padded_sequence = pad_sequences(sequence, maxlen=max_length)

    prediction = model.predict(padded_sequence)[0][0]

    return [prediction, "spam" if prediction >= 0.5 else "ham"]
text = "sale today! to stop texts call 98912460324"
print(predict_message(text))

# Run this cell to test your function and model. Do not modify contents.
def test_predictions():
  test_messages = ["how are you doing today",
                   "sale today! to stop texts call 98912460324",
                   "i dont want to go. can we try it a different day? available sat",
                   "our new mobile video service is live. just install on your phone to start watching.",
                   "you have won £1000 cash! call to claim your prize.",
                   "i'll bring it tomorrow. don't forget the milk.",
                   "wow, is your arm alright. that happened to me one time too"
                  ]

  test_answers = ["ham", "spam", "ham", "spam", "spam", "ham", "ham"]
  passed = True

  for msg, ans in zip(test_messages, test_answers):
    prediction = predict_message(msg)
    if prediction[1] != ans:
      passed = False

  if passed:
    print("You passed the challenge. Great job!")
  else:
    print("You haven't passed yet. Keep trying.")

test_predictions()