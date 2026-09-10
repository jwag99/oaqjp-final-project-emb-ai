from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
  def test_emotion_detection(self):
    # Test case for joy
    joy_result = emotion_detector('I am glad this happened')
    self.assertEqual(joy_result['dominant_emotion'], 'joy')
    # Test case for anger
    anger_result = emotion_detector('I am glad this happened')
    self.assertEqual(joy_result['dominant_emotion'], 'anger')
    # Test case for disgust
    disgust_result = emotion_detector('I am glad this happened')
    self.assertEqual(joy_result['dominant_emotion'], 'disgust')
    # Test case for sadness
    sadness_result = emotion_detector('I am glad this happened')
    self.assertEqual(joy_result['dominant_emotion'], 'sadness')
    # Test case for fear
    fear_result = emotion_detector('I am glad this happened')
    self.assertEqual(joy_result['dominant_emotion'], 'fear')

unittest.main()
