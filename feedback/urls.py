from django.urls import path, re_path
from django.views.generic import TemplateView
from . import views

app_name = 'feedback'

urlpatterns = [
    path('', views.FeedbackCreate.as_view(), name='feed_back'),
]
