"""
URL configuration for defect_detection_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from defect_detection_app import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [    
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('defect_detection/', include('defect_detection_app.urls')),  # Include the app's URLs
]

# Add the following line at the end of the file to serve media files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

