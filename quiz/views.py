from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Quiz

# Create your views here.

def quiz_list(request):
    quizes = Quiz.objects.all()
    return render(request, 'quiz/quizes.html', {'quizes': quizes})

def question_list(request, slug):
    questions = Question.objects.all()
    return render(request, 'quiz/questions.html', {'questions': questions})
