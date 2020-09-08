from django.urls import path, re_path
from . import views

app_name = 'accounts'

urlpatterns = [
    path(r'signup/', views.signup_view, name='signup'),
    path(r'login/', views.login_view, name='login'),
    #path('quiz/', views.question_list, name='quiz_name'),
    #re_path(r'^(?P<slug>[\w-]+)/$', views.question_list, name='question_list'),
    #path('<slug:slug>/', views.question_list),
]
