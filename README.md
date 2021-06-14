# dog_breed_classification


This model can be used to predict the breeds of dogs. 
Created a Rest api with Django Rest Framework that takes the input image in base64 and returns a jsonresponse having the breed and score predicted.
If the breed of dog is not predicted with score greater than 0.7 then it will show the result and message that "The dog does not match with anyone in the database"

The api is deployed to heroku: https://gb-dbc.herokuapp.com/dog_breed_api/
I implemented the get method to the api in case the api is directly called in which case user can choose the image and upload it for prediction.

Create a Models folder in dog_breed_classification folder and save the json file and weights file there.
The trained ResNet50 model json file and weights can be downloaded form below link :
https://drive.google.com/drive/folders/1x5Fky6Cc_67fUMEa6us2ffn9GWEAqzMi?usp=sharing
