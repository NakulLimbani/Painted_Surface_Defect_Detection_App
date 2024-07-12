from pyexpat.errors import messages
from django.shortcuts import render
from defect_detection_app.forms import ImageUploadForm
from defect_detection_app.models import Image, DefectClassification, Feedback
from defect_detection_app.utils import detect_defect
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            # Perform defect detection using your machine learning model
            classification, maximum_width, severity = detect_defect(image.image_file.path)
            image_classification = DefectClassification.objects.create(image=image, classification=classification, maximum_width=maximum_width, severity=severity)
            # Save the classification along with the image in the database
            image_classification.save()
            if maximum_width != None:
                maximum_width = round(maximum_width, 3)
            return render(request, 'upload_success.html', {'image': image, 'classification': classification, 'maximum_width': maximum_width, 'severity': severity})
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def upload_success(request):
    return render(request, 'upload_success.html')

def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        feedback = Feedback(name=name, email=email, message=message)
        feedback.save()
        return HttpResponse('<script>alert("Thank you for your feedback!"); window.location.href = "/";</script>')
        #return HttpResponse('Thank you for your feedback!')

    return render(request, 'contact_us.html')


"""
def live_detection(request):
    return render(request, 'live_detection.html')

"""

from django.shortcuts import render
from defect_detection_app.utils import live_defect_detection, start_live_detection, stop_live_detection
import cv2
import base64
import numpy as np
from django.http import JsonResponse


def live_detection(request):
    global results
    results = {
        'classification': '',
        'max_width': '',
        'severity': ''
    }

    if request.method == 'POST' and 'start_detection' in request.POST:
        start_live_detection()
    elif request.method == 'POST' and 'stop_detection' in request.POST:
        stop_live_detection()

    return render(request, 'live_detection.html', {'results': results})



def get_live_frame(request):
    global live_frame
    if live_frame:
        return JsonResponse({'frame': live_frame})
    return JsonResponse({})

