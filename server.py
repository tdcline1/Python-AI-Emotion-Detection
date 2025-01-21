"""
server.py

This module creates a Flask-based web application for detecting emotions 
in a given text using the `emotion_detector` function. The application 
provides an interface to input text and retrieve emotion analysis results, 
including individual emotion scores and the dominant emotion.

Routes:
- `/emotionDetector`: Receives text via a GET request, analyzes it using 
  the `emotion_detector` function, and returns the emotion scores and 
  dominant emotion. If the input text is invalid, an error message is returned.
  
- `/`: Serves the main application page (`index.html`) for user interaction.

Functions:
- emotion_detect(): Processes text input from the user, performs emotion 
  detection, and returns the results or an error message.

- render_index_page(): Renders the main HTML interface for the application.

Main Entry:
- If executed as the main module, the Flask application is started 
  on `0.0.0.0:5000`.

"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def emotion_detect():
    ''' This code receives the text from the HTML interface and
        runs emotion detection over it using emotion_detection()
        function. The output returned shows the dominant emotion
        as well as each emotion score.
    '''
    # Retrieve the text input from the HTTP GET request parameters with the key 'textToAnalyze'
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)
    #check for empty input
    if result['dominant_emotion'] is None:
        return "Invalid text! Try again."
    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
