"""
Flask Server
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion detection")

@app.route("/")
def render_index_page():
    """
    Render index page
    """
    return render_template("index.html")

@app.route("/emotionDetector")
def sent_detector():
    """
    Analize input text
    """
    text_to_analyze = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyze)
    anger = result["anger"]
    disgust = result["disgust"]
    fear = result["fear"]
    joy = result["joy"]
    sadness = result["sadness"]
    dominant_emotion = result["dominant_emotion"]
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return f"""For the given statement, the system response is
     'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 
     'sadness': {sadness}. The dominant emotion is {dominant_emotion}."""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 5000)
