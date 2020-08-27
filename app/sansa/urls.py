"""sansa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include

from sensors import views
from components import views as rviews
from sansa import views as firstviews
from users import views as uviews
from thsensors import views as dhtview
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hum/', views.indexHum, name='index'),
    path('temp/',views.viewTemp),
    path('luz/', rviews.index, name='index'),
    path('luz/prepare/',rviews.preparePins),
    path('luz/start/<int:pin>/',rviews.start,name='start'),
    path('luz/up/<int:pin>/', rviews.up, name="up"),
    path('luz/down/<int:pin>/', rviews.down, name="down"),
    path('luz/status/<int:pin>/', rviews.status, name="status"),
    path('date/', firstviews.date_time),
    path(r'^api-auth/', include('rest_framework.urls')),
    #api
    path('temp/algo/', views.unPost),
    path('user',uviews.ver),
    path('sensor/<slug:slug>/',dhtview.view)
]
