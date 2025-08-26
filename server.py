from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotion_detector

# Initialize the Flask app
app = Flask(__name__)

# Route for homepage
@app.route("/")
def index():
    return render_template("index.html")

# Route for emotion detection
@app.route("/emotionDetector", methods=["POST"])
def detect_emotion():
    text_to_analyze = request.form.get("text") or request.json.get("text")
    
    if not text_to_analyze:
        return jsonify({"error": "No text provided"}), 400
    
    result = emotion_detector(text_to_analyze)
    return jsonify(result)


if __name__ == "__main__":
    # Deploy on localhost:5000
    app.run(host="127.0.0.1", port=5000, debug=True)
