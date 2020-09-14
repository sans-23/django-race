from django.urls import path, re_path
from django.views.generic import TemplateView
from . import views

app_name = 'leaderboard'

urlpatterns = [
    path('', views.dummy),

]
