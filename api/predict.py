from fastapi import APIRouter
from typing import List, Union
from schema.pydantic_predict import PredictResponse, PredictData, PredictItem, PredictRequest
from core.prediction import predict_severity
from core.utils import init_model

router = APIRouter(tags=["Prediction"])

model_dir = "model"
model, tokenizer, id2label = init_model(model_dir)

@router.post("/predict", response_model=PredictResponse, summary="Predict complaint severity")
def predict_endpoint(request: PredictRequest, use_cache: bool = True):
    try:
        results = predict_severity(model, tokenizer, id2label, request.texts, use_cache=use_cache)
        # Normalize to list if single input
        if isinstance(results, dict) and "severity" in results:
            results_list = [results]
        else:
            results_list = results
        return PredictResponse(
            status="success",
            data=PredictData(predictions=[PredictItem(**r) for r in results_list])
        )
    except Exception as e:
        return PredictResponse(
            status="error",
            data=PredictData(predictions=[]),
            errors=[str(e)]
        )
