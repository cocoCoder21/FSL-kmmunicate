from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, StreamingHttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.templatetags.static import static
from django.conf import settings
from django.template import loader
import tensorflow as tf
import numpy as np
import json
import os


# ===================== VARIABLES  & CLASSES ==========================

with open(os.path.join(settings.STATIC_DIR, 'k_app\model_FSL.json'), 'r') as file1:
    model = file1.read()
    fsl_model = tf.keras.models.model_from_json(model)

fsl_model.load_weights(os.path.join(settings.STATIC_DIR, 'k_app\model_FSL.h5'))

keypoints_dict = {}

class detection(object):

    def __init__(self):
        # self.dataset = fsl_dataset   #DICTIONARY - fsl_dataset['a']["10"][10]
        self.model = fsl_model
        self.hand_response = []
        self.action_labels = np.array(['a', 'b', 'c'])
        self.res = []
        self.result = 'hold'
<<<<<<< HEAD
        self.threshold = 0.999
=======
        self.threshold = 0.9999
        self.keypoints_lookup = keypoints_dict

    def is_value_exist(self):
        for k,v in keypoints_dict.items():
            if self.hand_response in v:
                self.result = k
                return True
            else:
                return False
    
    def is_key_exist(self):
        for k,v in keypoints_dict.items():
            if self.hand_response in k:

                return True
            else:
                return False
>>>>>>> 5faf8c808dac1e721ff9a11b12a0ea73df594f46

    def fsl_predict(self):
        self.res = self.model.predict(
            np.expand_dims(self.hand_response, axis=0))[0]

        if self.res[np.argmax(self.res)] > self.threshold:
            self.result = str(self.action_labels[np.argmax(self.res)])

        else:
            self.result = "Please try again"

    def get_predictions(self, hand_response):
        
        self.hand_response = hand_response
        check = np.array(self.hand_response)
<<<<<<< HEAD

        # NO HANDS CHECKER
        if np.argmax(check) == 0:
            # print('NO HANDS!')
            self.result = "No hands detected"
=======
       
        #NO HANDS CHECKER
        # if np.argmax(check) == 0:
        #     # print('NO HANDS!')
        #     self.result =  "No hands detected"
        # else:
        #     if self.hand_response in self.keypoints_lookup:
        #         self.result = list(keypoints_dict.keys())[list(keypoints_dict.values()).index(self.hand_response)]
        #         print("AWIEEEEEE!!!")
        #     else:
        #         self.fsl_predict()
        #         keypoints_dict[self.result].append(self.hand_response)
        print("DICT: ",keypoints_dict)
        if self.is_value_exist():
            print('keypoint already cached.')

        elif np.argmax(check) == 0:
            keypoints_dict["No hands detected"] = []
            keypoints_dict["No hands detected"].append(self.hand_response)
            self.result ="No hands detected"
            
>>>>>>> 5faf8c808dac1e721ff9a11b12a0ea73df594f46
        else:
            self.fsl_predict()
<<<<<<< HEAD
=======

            if self.result in keypoints_dict.keys():
                keypoints_dict[self.result].append(self.hand_response)
            else:
                keypoints_dict[self.result] = []
                keypoints_dict[self.result].append(self.hand_response)
            


>>>>>>> 5faf8c808dac1e721ff9a11b12a0ea73df594f46


# =========================== MY VIEWS ===============================

def index(request):
    return render(request, 'k_app/landing.html')


# @csrf_protect
@csrf_exempt
def kcam(request):

    return render(request, 'k_app/cam_page.html')


def result(request):

    if request.method == 'POST':
        # print(request.POST['keypoints'])
        hand_response = request.POST['keypoints'].split(',')
        # print("LENGTH : ",hand_response)  #THE COMMA'S ARE INCUDED AS STRING, FIX THIS SOON!

        # raw_keypoints = [float(num)
        #                  for num in list(hand_response) if num != ',']
        raw_keypoints = []

        def recurrsion(listing):

            raw_keypoints.append(float(listing[0]))

            if len(listing) == 1:
                return listing
            else:
                return recurrsion(listing[1:])
        recurrsion(hand_response)

        # print(raw_keypoints, len(raw_keypoints))
        p = detection()
        p.get_predictions(raw_keypoints)
        print(p.result)
        # return render(request, 'k_app/kcam.html', {'signs': p.result})
        return HttpResponse(json.dumps({'signs': p.result}))

        # FUNCTION : This also reload the page, so find a way stay on the page.

    # return render(request, 'k_app/kcam.html', {'signs': p.result}) #, {'form': x} #,


# # else:
#     #     pass
#         # return()

#         #THROWS ValueError: Input 0 of layer "sequential" is incompatible
#         # with the layer: expected shape=(None, 126), found shape=(None, 1369)

#         #FUNCTION : This also reload the page, so find a way stay on the page.

#     return render(request, 'k_app/kcam.html', {'signs': p.result}) #, {'form': x} #,


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

        # play mp3 file
        # os.system("start os.path.join(settings.STATIC_DIR, 'k_app/fsl_audio.mp3')")
        # os.system('fsl_audio.mp3')

  # keyForm = forms.KeypointForm()
  # print(type(request.body))

# =============TEXT TO SPEECH =======================
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
