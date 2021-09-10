"""doctor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('doctor/',views.doctor),
    path('insert1/',views.insert1),
    path('patient/',views.patient),
    path('insert2/',views.insert2),
    path('specialization/',views.specialization),
    path('insert3/',views.insert3),
    path('viewdoctor/',views.viewdoctor),
    path('viewpatient/',views.viewpatient),
    path('gsalary/',views.gsalary),
    path('search/',views.search),
    path('sp/',views.view_special),

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
