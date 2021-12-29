from typing import Sequence
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, StreamingHttpResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.templatetags.static import static
from django.http import JsonResponse
from django.conf import settings
from django.template import loader
# from keras.models import model_from_json
import tensorflow as tf
import mediapipe as mp
import numpy as np
import json
import os
# from django.core import serializers
# from . import forms
# from gtts import gTTS


# ===================== VARIABLES  & CLASSES ==========================

with open(os.path.join(settings.STATIC_DIR, 'k_app/model.json'), 'r') as file1:
    model = file1.read()
    fsl_model = tf.keras.models.model_from_json(model)

#holistic model
mp_holistic = mp.solutions.holistic 

        
class detection(object):

    def __init__(self):
        # self.dataset = fsl_dataset   #DICTIONARY - fsl_dataset['a']["10"][10]
        self.mp_holistic = mp_holistic 
        self.model = fsl_model
        self.sequence = []
        self.predictions = []
        self.action_labels = np.array(['a','b','c'])
        self.res = []
        self.result = 'hold'


    def fsl_predict(self):
        self.res = self.model.predict(np.expand_dims(self.sequence, axis=0))[0]
        self.predictions.append(np.argmax(self.res))

        # print("PREDICTION : ", self.action_labels[np.argmax(self.res)])
        self.result = str(self.action_labels[np.argmax(self.res)])

    # def fsl_to_speech(self):
    #     language = 'en'
    #     output = gTTS(text=self.result, lang=language, slow=False)

    #     #save gTTS to mp3
    #     # output.save(os.path.join(settings.STATIC_DIR, 'k_app/fsl_audio.mp3'))
    #     try:
    #         os.remove("static/fsl_audio.mp3")
    #     except OSError:
    #         pass

    #     output.save('static/fsl_audio.mp3')
        # music = 'ok'
        # context = {
        #     'music': music,
        # }

        # return context

        #play mp3 file
        # os.system("start os.path.join(settings.STATIC_DIR, 'k_app/fsl_audio.mp3')")
        # os.system('fsl_audio.mp3')



    def get_predictions(self, hand_response):

        self.sequence = hand_response
        self.sequence = self.sequence[-30:]

        check = np.array(self.sequence)
       

        #NO HANDS CHECKER
        if np.argmax(check) == 0:
            # print('NO HANDS!')
            self.result =  "NOHANDS"
        else:

            self.fsl_predict()
            


# Create your views here.

def index(request):
    return render(request,'k_app/index.html')

# @csrf_protect
@csrf_exempt 
def kcam(request):
    # keyForm = forms.KeypointForm()
    # print(type(request.body))
    p = detection()
    if request.method == "POST":
        
        req = request.body
        post_result = json.loads(req.decode('utf-8'))
        hand_response = post_result['handResponse']
        p.get_predictions(hand_response)
    
    signs= {
        'sign':p.result
    }

    sign_json = json.dumps(signs)

    #=============TEXT TO SPEECH =======================
    # p.fsl_to_speech()

    # print(type(post_result))
        # H_SIGN = 
        # keyForm['sign'].value = H_SIGN

    # print(type(sign_json))
    # print(type(signs['sign']))
        # sign_json = json.dumps(signs)
    # print(type(keyForm['sign'].value))
    # print("HELLOW >> ", signs['sign'])
    # else:
    #     print('GET GET AWW!')

    # request.session['H_SIGN '] = p.get_predictions(hand_response)
    #     return render(request,'k_app/kcam.html')
        # sign['signs'] = H_SIGN
        # print(sign['signs'])
        # render(HttpResponse(sign))
        # return HttpResponse(sign['signs'],  content_type="text/plain")

         # t = Template("SIGN : {{ sign }}.")
        # c = Context({"sign": sign})
        # render(HttpResponse(Context({'signs':sign})))
        # template = loader.get_template('k_app/kcam.html')
        # return HttpResponse(template.render(sign, request))
        # print(sign['signs'])
        
        # sign_res = serializers.serialize("json", sign)
        # return JsonResponse(sign_res, content_type='application/json', safe=False)
        # html = '<div>Hello World</div>'
        # return JsonResponse({"data": html, "message": "your message"})

        # html = "<h4>{sign.s}</h4>"
        # return HttpResponse(html, content_type='text/html')
    print('content : ', sign_json, 'type : ', type(sign_json))
    return render(request, 'k_app/kcam.html', {"signs":p.result}) #, {"signs":sign_json}









