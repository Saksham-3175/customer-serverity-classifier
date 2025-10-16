import pickle, json, tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences

with open("artifacts/severity_lstm_tf_tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)
with open("artifacts/severity_lstm_tf_labels.json") as f:
    label_maps = json.load(f)
model = tf.keras.models.load_model("artifacts/severity_lstm_tf.keras")

MAX_LEN = 160
id2label = label_maps["id2label"]

def predict_severity(text):
    seq = tokenizer.texts_to_sequences([text])
    pad = pad_sequences(seq, maxlen=MAX_LEN)
    probs = model.predict(pad)
    label = id2label[str(probs.argmax(axis=1)[0])]
    confidence = float(probs.max())
    return {"severity": label, "confidence": confidence}
