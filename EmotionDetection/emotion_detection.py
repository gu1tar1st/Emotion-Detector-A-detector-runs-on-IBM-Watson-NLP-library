import requests, json


def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myObj =  { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, headers = header, json = myObj)
    #formatted = json.loads(response.text)
    #dominant_emotion = max(formatted['emotionPredictions'][0]['emotion'], key=formatted['emotionPredictions'][0]['emotion'].get)
    return response.text


# response = emotion_detector("I hate working long hours")
# formatted = json.loads(response)
# anger_score = formatted['emotionPredictions'][0]['emotion']['anger']
# disgust_score = formatted['emotionPredictions'][0]['emotion']['disgust']
# fear_score = formatted['emotionPredictions'][0]['emotion']['fear']
# joy_score = formatted['emotionPredictions'][0]['emotion']['joy']
# sadness_score = formatted['emotionPredictions'][0]['emotion']['sadness']
# dominant_emotion = max(formatted['emotionPredictions'][0]['emotion'], key=formatted['emotionPredictions'][0]['emotion'].get)
# print({'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score, 'dominant_emotion': dominant_emotion})