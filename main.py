from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

sentiment_analyzer = pipeline("sentiment-analysis")

class TextRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    sentiment: str
    confidence: float

@app.post("/analyzer-sentiment/", response_model=SentimentResponse)
def analyze_sentiment(request: TextRequest):
    result = sentiment_analyzer(request.text)[0]
    sentiment = result['label']
    confidence = result['score']

    return SentimentResponse(sentiment=sentiment, confidence=confidence)