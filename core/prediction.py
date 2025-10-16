import time
import numpy as np
from typing import List, Union, Dict, Any
from core.preprocessing import clean_text, to_seq, preprocess_with_cache
from core.cache import load_cache, save_cache
from core.logging import setup_logging
import logging

logger = logging.getLogger("myapp")
setup_logging()

def predict_severity(
    model,
    tokenizer,
    id2label,
    texts: Union[str, List[str]],
    use_cache: bool = True,
    ttl_minutes: int = 30
) -> Union[Dict[str, Any], List[Dict[str, Any]]]:

    single_input = False
    if isinstance(texts, str):
        texts = [texts]
        single_input = True
    elif not isinstance(texts, list):
        return {"error": "Input must be a string or list of strings."}

    results = []
    try:
        preprocessed_list = []
        for t in texts:
            try:
                preproc = preprocess_with_cache(t, tokenizer, use_cache=use_cache, ttl_minutes=ttl_minutes)
                preprocessed_list.append(preproc)
            except Exception as e:
                logger.error(f"Preprocessing failed for text: {t[:50]}..., error: {e}")
                results.append({"error": f"Preprocessing failed: {str(e)}"})
                continue

        if not preprocessed_list:
            return {"error": "No valid text to predict."}

        seqs = np.array([p["sequence"] for p in preprocessed_list])
        start_time = time.time()
        probs_batch = model.predict(seqs, verbose=0)
        elapsed_ms = (time.time() - start_time) * 1000  

        for i, probs in enumerate(probs_batch):
            if "error" in results[i] if i < len(results) else {}:
                continue
            pred_id = int(np.argmax(probs))
            results.append({
                "severity": id2label[pred_id],
                "confidence": round(float(np.max(probs)) * 100, 2),
                "prediction_time_ms": round(elapsed_ms / len(texts), 2)
            })

    except Exception as e:
        logger.error(f"Prediction failed: {e}")
        return {"error": str(e)}

    return results[0] if single_input else results
