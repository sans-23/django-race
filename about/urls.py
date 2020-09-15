from django.urls import path, re_path
from django.views.generic import TemplateView
from . import views

app_name = 'about'

urlpatterns = [
    path('', views.about, name='about_app'),
]
