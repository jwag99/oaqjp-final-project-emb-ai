""" Emotion Detection """
import requests
import json

def emotion_detector(text_to_analyze):
  """ emotion_detector function

  Dependency: WATSON AI Lib
  Input: Text to analyze
  Output: JSON emotion analysis of text
  """

  url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
  headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
  inputObj = { "raw_document": { "text": text_to_analyze } }
  response = requests.post(url, json=inputObj, headers=headers)
  formatted_response = json.loads(response.text)
  emotions = formatted_response['emotionPredictions'][0]['emotion']
  dominant_emotion = "none"
  dom_score = 0
  for emotion, score in emotions.items():
    if score > dom_score:
      dom_score = score
      dominant_emotion = emotion
  emotions['dominant_emotion'] = dominant_emotion
  return emotions
