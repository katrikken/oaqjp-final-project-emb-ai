from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotion_detector

# Initialize the Flask app
app = Flask(__name__)

# Route for homepage
@app.route("/")
def index():
    return render_template("index.html")

# Route for emotion detection
@app.route("/emotionDetector")
def detect_emotion():
    text_to_analyze = request.args.get("textToAnalyze")
    
    if not text_to_analyze:
        return jsonify({"error": "No text provided"}), 400
    
    result = emotion_detector(text_to_analyze)
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
