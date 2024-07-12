from django.contrib import admin
from .models import Image, DefectClassification, Feedback

# Register your models here.

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_file', 'upload_date']
    # Add other configurations as needed

@admin.register(DefectClassification)
class DefectClassificationAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'classification']
    

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']




