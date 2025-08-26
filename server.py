"""
server.py

Flask web application for emotion detection using the Watson NLP API.

This module provides:
- A homepage route ("/") that renders the 'index.html' template.
- An emotion detection route ("/emotionDetector") that accepts text input
  via query parameters, processes it with the EmotionDetection package,
  and returns a formatted string of emotion scores and the dominant emotion.

Usage:
    Run this module to start the web server on localhost:5000:
        python3 server.py

Dependencies:
    - Flask
    - EmotionDetection package (custom)
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

# Initialize the Flask app
app = Flask(__name__)

# Route for homepage
@app.route("/")
def index():
    """
    Render the homepage of the web application.

    Returns:
        str: Rendered HTML content from 'index.html' template.
    """

    return render_template("index.html")

# Route for emotion detection
@app.route("/emotionDetector")
def detect_emotion():
    """
    Detect emotions in the given text using Watson NLP API.

    Args:
        text_to_analyze (str): The input text to be analyzed for emotions.

    Returns:
        dict: A dictionary containing scores for anger, disgust, fear, joy, sadness,
              and the dominant emotion.
    """

    text_to_analyze = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyze)

    # Handle invalid/blank input
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    # Format the response into a readable string
    response_str = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_str


if __name__ == "__main__":
    # Deploy on localhost:5000
    app.run(host="127.0.0.1", port=5000, debug=True)
