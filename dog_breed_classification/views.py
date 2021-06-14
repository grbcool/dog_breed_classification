from django.shortcuts import render, redirect

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
#from rest_framework.parsers import FileUploadParser
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse


import base64
from PIL import Image
import io
import os
import requests
import json
import numpy as np
import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import model_from_json

base_path=os.path.abspath(os.path.dirname(__file__))

@api_view(['GET','POST'])
def model(request):
    if request.method=='GET':
        context={}
        return render(request,'input.html',context)
    elif request.method=='POST':
        data = request.data
        
        img_bytes = base64.b64decode(str(data['img']))
        img_file = io.BytesIO(img_bytes)
        img_pil = Image.open(img_file)
        img = img_to_array(img_pil,data_format='channels_last')
        img = tf.image.resize(img,(224,224))
        
        img = np.expand_dims(img,axis=0)
        img=img[:,:,:,:3]
        model_json_file = os.path.join(base_path,'models/model.json')
        model_weights_file = os.path.join(base_path,'models/model_weights.h5')
        with open(model_json_file,'r') as json_file:
            model = model_from_json(json_file.read())
        model.load_weights(model_weights_file)
        labels=['beagle', 'chihuahua', 'doberman', 'french_bulldog',
       'golden_retriever', 'malamute', 'pug', 'saint_bernard',
       'scottish_deerhound', 'tibetan_mastiff']
        
        pred = model.predict(img)
        if np.max(pred)>0.7:
            prediction={
                "breed":labels[np.argmax(pred)],
                "score": np.max(pred)*100   
            }
        else:
            prediction={
                "result": np.hstack((np.reshape(np.array(labels),(10,1)),pred.T)).tolist(),
                "message":"The dog does not match with anyone in the database"    
            }  
        return Response(prediction)         
        


               




def convert(request):
    
    img = request.FILES['image']
    #encoding = Image.open(img)
    #with open(img,'rb') as img_bytes:
    #    encoding=base64.b64encode(img_bytes.read())
    encoding=base64.b64encode(img.read())    
    encoding=encoding.decode('utf-8')    
    #url = "http://127.0.0.1:8000/dog_breed_api/"
    url = "https://gb-dbc.herokuapp.com/dog_breed_api/"
    payload={"img":encoding}   
    headers = {
        'Content-Type': 'application/json'
    }
    
    
    
    r=requests.post(url,json.dumps(payload),headers=headers)           
    
    return HttpResponse(r.content)
    

