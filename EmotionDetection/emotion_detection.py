
import json
import requests

# Watson Emotion API endpoint and model ID
URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}


def _empty_result():
    """
    Return a standardized 'empty' result used when text is invalid
    or the API cannot be reached.
    """
    return {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
    }


def emotion_detector(text_to_analyze: str):
    """
    Call the Watson NLP Emotion API and return a simplified result dict:

    {
        "anger": float | None,
        "disgust": float | None,
        "fear": float | None,
        "joy": float | None,
        "sadness": float | None,
        "dominant_emotion": str | None,
    }

    - If the text is empty/invalid → all None.
    - If the API call fails (timeout, SSL, no internet, etc.) → all None.
    """

    # Handle empty or whitespace-only input
    if not text_to_analyze or not text_to_analyze.strip():
        return _empty_result()

    payload = {"raw_document": {"text": text_to_analyze}}

    # Network-safe call: any error returns an empty result
    try:
        response = requests.post(URL, json=payload, headers=HEADERS, timeout=5)
    except Exception:
        return _empty_result()

    # IBM spec: 400 = invalid text
    if response.status_code == 400:
        return _empty_result()

    # Any other non-200 status → treat as failure
    if response.status_code != 200:
        return _empty_result()

    # Parse JSON safely
    try:
        data = json.loads(response.text)
        emotions = data["emotionPredictions"][0]["emotion"]
    except (ValueError, KeyError, IndexError, TypeError):
        return _empty_result()

    anger = emotions.get("anger", 0.0)
    disgust = emotions.get("disgust", 0.0)
    fear = emotions.get("fear", 0.0)
    joy = emotions.get("joy", 0.0)
    sadness = emotions.get("sadness", 0.0)

    # Find the dominant emotion
    scores = {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
    }
    dominant = max(scores, key=scores.get)

    return {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant,
    }

