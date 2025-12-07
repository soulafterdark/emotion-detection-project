"""
Flask server for the Watson NLP Emotion Detection web app.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def handle_emotion_detector():
    """
    Handles GET requests from the front-end JavaScript.

    Expects a query parameter named `textToAnalyze` and returns a
    formatted string summarizing all emotion scores and the
    dominant emotion.
    """
    text_to_analyze = request.args.get("textToAnalyze", "")

    result = emotion_detector(text_to_analyze)

    # If the model reports "no valid text", show the error message
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!."

    # Build the response string in the exact format IBM specifies
    response_text = (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} "
        f"and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_text


@app.route("/")
def render_index_page():
    """
    Render the main UI page.
    """
    return render_template("index.html")


if __name__ == "__main__":
    # Course spec: app should be available on localhost:5000
    app.run(host="0.0.0.0", port=5000)

