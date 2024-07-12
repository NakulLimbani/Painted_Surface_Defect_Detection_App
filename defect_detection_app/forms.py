from django import forms
from defect_detection_app.models import Image, Feedback

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image_file']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']
