import tensorflow as tf
import pickle
import json
import re
from pathlib import Path

DATA_DIR = Path("cache")
DATA_DIR.mkdir(parents=True, exist_ok=True)

MAX_LEN = 160 
URL_PAT = re.compile(r"https?://\S+|www\.\S+")
EMAIL_PAT = re.compile(r"\S+@\S+")
NONPRINT_PAT = re.compile(r"[^\x00-\x7F]+")

def load_model(model_path: str):
    return tf.keras.models.load_model(model_path)

def load_tokenizer(tokenizer_path: str):
    with open(tokenizer_path, "rb") as f:
        return pickle.load(f)

def load_label_maps(labels_path: str):
    with open(labels_path, "r") as f:
        info = json.load(f)
    label2id = info["label2id"]
    id2label = {int(k): v for k, v in info["id2label"].items()}
    return label2id, id2label

def init_model(model_dir: str):
    model = load_model(f"{model_dir}/severity_lstm_tf.keras")
    tokenizer = load_tokenizer(f"{model_dir}/severity_lstm_tf_tokenizer.pkl")
    _, id2label = load_label_maps(f"{model_dir}/severity_lstm_tf_labels.json")
    return model, tokenizer, id2label
