from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from django.db.models.query import QuerySet
import cv2
import numpy as np
import matplotlib.pyplot as plt

from .models import FacialExpressionModel

test_model = FacialExpressionModel("model.json", "model_weights.h5")

# Loading the classifier from the file.
facec = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def Emotion_Analysis(img):
    """ It does prediction of Emotions found in the Image provided, does the 
    Graphical visualisation, saves as Images and returns them """

    # Read the Image through OpenCv's imread()
    path = "media/images/" + str(img)
    image = cv2.imread(path)

    # Convert the Image into Gray Scale
    gray_frame = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Image size is reduced by 30% at each image scale.
    scaleFactor = 1.3

    # 5 neighbors should be present for each rectangle to be retained.
    minNeighbors = 5

    # Detect the Faces in the given Image and store it in faces.
    faces = facec.detectMultiScale(gray_frame, scaleFactor, minNeighbors)

    # When Classifier could not detect any Face.
    if len(faces) == 0:
        return [img]

    for (x, y, w, h) in faces:

        # Taking the Face part in the Image as Region of Interest.
        roi = gray_frame[y:y+h, x:x+w]

        # Let us resize the Image accordingly to use pretrained model.
        roi = cv2.resize(roi, (48, 48))

        # Let us make the Prediction of Emotion present in the Image
        prediction = test_model.predict_emotion(
            roi[np.newaxis, :, :, np.newaxis])

        # Custom Symbols to print with text of emotion.

    

        ## based on the prediction recommend music


        # Defining the Parameters for putting Text on Image
        Text = str(prediction) 
        print(Text)
      
    # Returns a list containing the names of Original, Predicted, Bar Plot Images
    return (Text)


# Create your views here.

def upload_img(request):
    if request.method == 'POST':
        form = ImageUpForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('show')
    else:
        form = ImageUpForm()
    return render(request, 'imgapp/cc1.html', {'form':form})


def success(request):
    return HttpResponse('Uploaded')

def cc(request):
    return render(request,'imgapp/cc1.html')
def display(request):
  
    if request.method == 'GET':
  
        # getting all the objects of hotel.
        Images = ImageUp.objects.latest('id')
        image_name = Images.filename()
        print(image_name)
        result = Emotion_Analysis(image_name)
        context = {}
        context['res']= result
        context['images']=Images
        return render(request, 'imgapp/display.html',
                     context)

def contact(request):
    return render(request,'imgapp/contact.html')