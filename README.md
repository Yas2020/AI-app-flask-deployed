# Repository for final project

You have been hired as a software engineer by an e-commerce company to create an AI-based web app that performs analytics on customer feedback for their signature products. To accomplish this requirement, you will create an Emotion Detection system that processes feedback provided by the customer in text format and deciphers the associated emotion expressed.

In this final project, you will be assessed on the knowledge gained on all aspects of app creation and its web deployment throughout this course. You will be required to save screenshots of your results from time to time, with specific nomenclature. These screenshots will have to be uploaded in the peer graded assignment that follows.

In this project, we use the embeddable Watson AI libraries to create an emotion detection application.

Emotion detection extends the concept of sentiment analysis by extracting the finer emotions, like joy, sadness, anger, and so on, from statements rather than the simple polarity that sentiment analysis provides. This makes emotion detection a very important branch of study and businesses use such systems widely for their AI based recommendation systems, automated chat bots, and so on.

The GitHub repository of the project is available on the URL mentioned below.
`https://github.com/ibm-developer-skills-network/oaqjp-final-project-emb-ai.git`

git clone this repo into a folder called `project_folder`.

 The Watson NLP libraries are embedded. Therefore, there is no need of importing them to your code. You only need to send a post request to the correct function in the library and receive the output. 
 Create `emotion_detection.py` that make this request and recievs the response. The URL, the headers, and the input json format is as follows

 `URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
Input json: { "raw_document": { "text": text_to_analyse } }`
 
 
 To handle possible errors, check the status code of the response from the server. In the case of a blank input and status_code=400 for bad request, return None for all categories. Otherwise 




 Create a Python package: make a folder called EmotionDetection, include `__init__.py` along with `emotion_detection.py`. To implement a unit test, create `test_emotion_detection.py` in the package folder. Make sure the following test cases pass:

 Statement	                               Dominant Emotion
I am glad this happened	                          joy
I am really mad about this	                      anger
I feel disgusted just hearing about this	      disgust
I am so sad about this	                          sadness
I am really afraid that this will happen	      fear


Create a `server.py` that run a flask server wich renedrs a html page as template. Run static code analysis on the code created. Use PyLint library on server.py file. 

Finally, Run the flask server (port 5000) and make single prediction. 

![alt text](images/Screenshot%202024-04-06%20at%206.05.28 PM.png)