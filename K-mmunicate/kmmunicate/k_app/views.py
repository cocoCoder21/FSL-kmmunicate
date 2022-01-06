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

with open(os.path.join(settings.STATIC_DIR, 'k_app\FSL_DST_MODEL2.json'), 'r') as file1:
    model = file1.read()
    fsl_model = tf.keras.models.model_from_json(model)

fsl_model.load_weights(os.path.join(settings.STATIC_DIR, 'k_app\FSL_DST_MODEL2.h5'))

keypoints_dict = {}


class detection(object):

    def __init__(self):
        # self.dataset = fsl_dataset   #DICTIONARY - fsl_dataset['a']["10"][10]
        self.model = fsl_model
        self.hand_response = []
        self.action_labels = np.array(['a', 'b', 'c'])
        self.res = []
        self.result = 'hold'
        self.threshold = 0.9999
        self.keypoints_lookup = keypoints_dict

    def is_value_exist(self):
        for k,v in keypoints_dict.items():
            if self.hand_response in v:
                self.result = k
                return True
            else:
                return False
                

    def fsl_predict(self):
        self.res = self.model.predict(np.expand_dims(self.hand_response, axis=0))[0]

        if np.amax(self.res) > self.threshold:
            self.result = str(self.action_labels[np.argmax(self.res)])

        else:
            self.result = "Please try again"

    def get_predictions(self, hand_response):
        
        self.hand_response = hand_response
        check = np.array(self.hand_response)

        if self.is_value_exist():
            print('keypoint already cached.')

        elif np.amax(check) == 0:
            keypoints_dict["No hands detected"] = []
            keypoints_dict["No hands detected"].append(self.hand_response)
            self.result ="No hands detected"
            
        else:
            self.fsl_predict()

            if self.result in keypoints_dict.keys():
                keypoints_dict[self.result].append(self.hand_response)
            else:
                keypoints_dict[self.result] = []
                keypoints_dict[self.result].append(self.hand_response)



# =========================== MY VIEWS ===============================

def index(request):
    return render(request, 'k_app/landing.html')


# @csrf_protect
@csrf_exempt
def kcam(request):

    return render(request, 'k_app/cam_page.html')


def result(request):

    if request.method == 'POST':
        hand_response = request.POST['keypoints'].split(',')
        raw_keypoints = []

        def recursion(listing):

            raw_keypoints.append(float(listing[0]))

            if len(listing) == 1:
                return listing
            else:
                return recursion(listing[1:])
        
        recursion(hand_response)

        p = detection()
        p.get_predictions(raw_keypoints)
        print(p.result)
    
        return HttpResponse(json.dumps({'signs': p.result}))
