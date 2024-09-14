import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = obj, headers = header)
    if response.status_code == 400:
        result = {'anger' : None,
        'disgust' : None,
        'fear' : None, 
        'joy' : None,
        'sadness' : None,
        'dominant_emotion' : None}
    else:
        formatted_text = json.loads(response.text)
        anger_score = formatted_text["emotionPredictions"][0]["emotion"]["anger"]
        disgust_score = formatted_text["emotionPredictions"][0]["emotion"]["disgust"]
        fear_score = formatted_text["emotionPredictions"][0]["emotion"]["fear"]
        joy_score = formatted_text["emotionPredictions"][0]["emotion"]["joy"]
        sadness_score = formatted_text["emotionPredictions"][0]["emotion"]["sadness"]
    
        result = {'anger' : anger_score,
        'disgust' : disgust_score,
        'fear' : fear_score, 
        'joy' : joy_score,
        'sadness' : sadness_score}
    
        dominant_emotion = max(result, key = result.get)
        result['dominant_emotion'] = dominant_emotion
        
    return result