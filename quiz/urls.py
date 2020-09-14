from django.urls import path, re_path
from django.views.generic import TemplateView
from . import views


app_name = 'quiz'

urlpatterns = [
    path('', views.quiz_list, name='quiz_list'),#safe
    #path('result/', views.result_page, name='result'),
    #path('quiz/', views.question_list, name='quiz_name'),

    path('lets/create/', views.QuizCreate.as_view(), name='quiz_create'),#safe
    path('myquiz/', views.MyQuiz, name='my_quiz'),#safe

    re_path(r'^main/(?P<slug>[\w-]+)/create/$', views.QuestionCreate.as_view(), name='question_create'),
    path('main/<int:pk>/update/', views.QuestionUpdate.as_view(), name='question_update'),#safe
    path('main/<int:pk>/delete/', views.QuestionDelete.as_view(), name='question_delete'),#safe


    re_path(r'^result/(?P<slug>[\w-]+)/$', views.result_page, name='result'),#safe
    re_path(r'^(?P<slug>[\w-]+)/exam/$', views.exam_view, name='exam'),#safe
    re_path(r'^(?P<slug>[\w-]+)/$', views.question_list, name='question_list'),#safe


]

#urlpatterns += static(settings.MEDIA_URL, documents_root=settings.MEDIA_ROOT)
