from django.urls import path
from defect_detection_app import views 


urlpatterns = [
    path('upload/', views.upload_image, name='upload_image'),
    path('upload/success/', views.upload_success, name='upload_success'),
    path('live/', views.live_detection, name='live_detection'),
    path('get_live_frame/', views.get_live_frame, name='get_live_frame'),
    path('contact_us/', views.contact_us, name='contact_us'),
    
]
