from pydantic import BaseModel, Field
from typing import List, Union


class PredictItem(BaseModel):
    severity: Union[str, None] = Field(None, description="Predicted severity label")
    confidence: Union[float, None] = Field(None, description="Confidence percentage")
    prediction_time_ms: Union[float, None] = Field(None, description="Time taken to predict in milliseconds")
    error: Union[str, None] = Field(None, description="Error message if prediction failed")


class PredictData(BaseModel):
    predictions: List[PredictItem] = Field(..., description="List of prediction results")


class PredictResponse(BaseModel):
    status: str = Field(..., description="Status of the response, e.g., 'success' or 'error'")
    data: PredictData = Field(..., description="Payload containing prediction results")
    errors: List[str] = Field(default_factory=list, description="List of error messages if any")

class PredictRequest(BaseModel):
    texts: Union[str, List[str]]