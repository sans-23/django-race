from django.urls import path, re_path
from django.views.generic import TemplateView
from . import views

app_name = 'leaderboard'

urlpatterns = [
    path('', views.my_attempts, name='attempts'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.report_card, name='reportcard'),
]
