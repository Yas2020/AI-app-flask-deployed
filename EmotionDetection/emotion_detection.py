import requests
import json


url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text):
    data = { "raw_document": { "text": text } }
    response = requests.post(url=url, json=data, headers=headers, timeout=2.5)
    predictions = json.loads(response.text)
    prediction = predictions.get('emotionPredictions')
    if response.status_code == 400:
        return ("For the given statement, the system response is 'anger': None" 
                " 'disgust': None, 'fear': None, 'joy': None and 'sadness': None." 
                " The dominant emotion is None.")

    res = prediction[0]['emotion']
    res['dominant_emotion'] = sorted(res, key=lambda x: res[x])[-1]
    return  (f"For the given statement, the system response is 'anger': " 
                  f"{res['anger']}, 'disgust': {res['disgust']}, 'fear': {res['fear']}, " 
                  f"'joy': {res['joy']} and 'sadness': {res['anger']}." 
                  f" The dominant emotion is {res['dominant_emotion']}.")

if __name__ == '__main__':
    print(emotion_detector('I love this'))