from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'quiz'

urlpatterns = [
    path('', views.quiz_list, name='quiz_list'),
    #path('result/', views.result_page, name='result'),
    #path('quiz/', views.question_list, name='quiz_name'),
    re_path(r'^result/(?P<slug>[\w-]+)/$', views.result_page, name='result'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.question_list, name='question_list'),

    #path('<slug:slug>/', views.question_list),
]

#urlpatterns += static(settings.MEDIA_URL, documents_root=settings.MEDIA_ROOT)
