"""
test_emotion_detection.py

This module contains unit tests for the `emotion_detector` function from the 
`EmotionDetection.emotion_detection` module. The tests verify that the function 
correctly identifies the dominant emotion for various text inputs.

Classes:
- TestEmotionDetection: A unittest.TestCase subclass that defines test cases 
  for validating the functionality of the `emotion_detector` function.

Methods:
- test_emotion_detector(): Tests the `emotion_detector` function with 
  representative inputs for each emotion (joy, anger, disgust, sadness, fear) 
  and checks whether the correct dominant emotion is returned.

Execution:
- When run directly, the script executes the unit tests using `unittest.main()`.
"""

from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        # Test case for joy
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'], 'joy')

        # Test case for anger
        result_1 = emotion_detector('I am really mad about this')
        self.assertEqual(result_1['dominant_emotion'], 'anger')

        # Test case for disgust
        result_1 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_1['dominant_emotion'], 'disgust')

        # Test case for sadness
        result_1 = emotion_detector('I am so sad about this')
        self.assertEqual(result_1['dominant_emotion'], 'sadness')

        # Test case for feaar
        result_1 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_1['dominant_emotion'], 'fear')

unittest.main()
