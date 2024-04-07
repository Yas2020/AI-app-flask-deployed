from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector


app = Flask(__name__)

@app.route('/')
def index():
    "Renders the main index page"
    
    return render_template("index.html")

@app.route('/emotionDetector')
def emotion():
    "Calls the api and returns the emotion prediction"

    req = request.args.get('textToAnalyze')
    return emotion_detector(req)
