from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.templatetags.static import static
from django.http import JsonResponse
from django.conf import settings
from django.template import loader
import tensorflow as tf
import numpy as np
import json
import os
import h5py


# ===================== VARIABLES  & CLASSES ==========================

with open(os.path.join(settings.STATIC_DIR, 'k_app\model_FSL.json'), 'r') as file1:
    model = file1.read()
    fsl_model = tf.keras.models.model_from_json(model)

fsl_model.load_weights(os.path.join(settings.STATIC_DIR, 'k_app\model_FSL.h5'))



class detection(object):

    def __init__(self):
        # self.dataset = fsl_dataset   #DICTIONARY - fsl_dataset['a']["10"][10]
        self.model = fsl_model
        self.hand_response = []
        self.action_labels = np.array(['a','b','c'])
        self.res = []
        self.result = 'hold'
        self.threshold = 0.999


    def fsl_predict(self):
        self.res = self.model.predict(np.expand_dims(self.hand_response, axis=0))[0]

        # print("SHAPE : ", self.res.shape)
        print(self.res[np.argmax(self.res)])
        if self.res[np.argmax(self.res)] > self.threshold: 
            self.result = str(self.action_labels[np.argmax(self.res)])
            print(self.result)
        else:
            self.result = "Please try again"
      

    def get_predictions(self, hand_response):

        self.hand_response = hand_response
        check = np.array(self.hand_response)
       
        #NO HANDS CHECKER
        if np.argmax(check) == 0:
            # print('NO HANDS!')
            self.result =  "No hands detected"
        else:

            self.fsl_predict()
            


# =========================== MY VIEWS ===============================

def index(request):
    return render(request,'k_app/index.html')


# @csrf_protect
@csrf_exempt 
def kcam(request):

    
    if request.method == "POST":
        
        req = request.body
        # print(req)
        post_result = json.loads(req.decode('utf-8'))
        hand_response = post_result['handResponse']
        
        p = detection()
        p.get_predictions(hand_response) 
        
        s = p.result
        print("RESULT  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ", p.result)
    # signs= {
    #     'sign':p.result
    # }

    # sign_json = json.dumps(signs)

    
    return render(request, 'k_app/kcam.html') #, {"signs":sign_json}
    #, {"signs":p.result}


def result(request):
    x = kcam.s
    print(x)









#from django.views.decorators.csrf import csrf_protect
# from django.core import serializers
#import mediapipe as mp
# from gtts import gTTS
# from . import forms



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





  # keyForm = forms.KeypointForm()
  # print(type(request.body))

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
    # print('content : ', sign_json, 'type : ', type(sign_json))



