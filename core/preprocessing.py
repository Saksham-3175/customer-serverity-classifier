import re
from tensorflow.keras.preprocessing.sequence import pad_sequences
from core.utils import MAX_LEN, URL_PAT, EMAIL_PAT, NONPRINT_PAT
from core.cache import load_cache, save_cache
from core.logging import setup_logging
import hashlib

logger = setup_logging()

def clean_text(text: str) -> str:
    text = text.lower()
    text = URL_PAT.sub(" ", text)
    text = EMAIL_PAT.sub(" ", text)
    text = NONPRINT_PAT.sub(" ", text)
    text = re.sub(r"[^a-z0-9\s\.\,\!\?\$]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def to_seq(tokenizer, texts):
    return pad_sequences(tokenizer.texts_to_sequences(texts), maxlen=MAX_LEN, padding="post")


def preprocess_with_cache(text: str, tokenizer, use_cache: bool = True, ttl_minutes: int = 30):
    cache_key = "preproc_" + hashlib.md5(text.encode("utf-8")).hexdigest()
    if use_cache:
        cached = load_cache(cache_key, ttl_minutes=ttl_minutes)
        if cached:
            logger.debug(f"Cache hit for text: {text[:30]}...")
            return cached
        else:
            logger.debug(f"Cache miss for text: {text[:30]}...")
    try:
        cleaned = clean_text(text)
        sequence = to_seq(tokenizer, [cleaned])[0].tolist()
        result = {"cleaned": cleaned, "sequence": sequence}
        if use_cache:
            save_cache(cache_key, result, ttl_minutes=ttl_minutes)
        return result
    except Exception as e:
        logger.error(f"Error preprocessing text: {text[:30]}..., error: {e}")
        raise e

