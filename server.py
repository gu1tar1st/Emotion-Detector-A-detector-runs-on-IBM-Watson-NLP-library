from flask import Flask, render_template, request
import requests, json
from EmotionDetection.emotion_detection import emotion_detector as eDetect
app = Flask("__emotionDetector__")


@app.route("/emotionDetector", methods=["GET"])
def indexPage():
    return render_template('index.html')


@app.route("/emotionDetector", methods=["POST"])
def emotionDetector():
    text = request.args.get("textToAnalyze")

    # Handle blank input
    if not text or text.strip() == "":
        # Return dictionary with None values for status_code 400
        result = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
        return json.dumps(result), 400

    # Call emotion detection function
    responseText = eDetect(text)
    formatted = json.loads(responseText)

    # Extract emotion scores
    emotion_scores = formatted['emotionPredictions'][0]['emotion']
    anger_score = emotion_scores['anger']
    disgust_score = emotion_scores['disgust']
    fear_score = emotion_scores['fear']
    joy_score = emotion_scores['joy']
    sadness_score = emotion_scores['sadness']
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Construct result string
    result = (
        f"For the given statement, the system response is "
        f"'anger': {anger_score}, "
        f"'disgust': {disgust_score}, "
        f"'fear': {fear_score}, "
        f"'joy': {joy_score} and "
        f"'sadness': {sadness_score}. "
        f"The dominant emotion is <b>{dominant_emotion}</b>."
    )

    return result, 200