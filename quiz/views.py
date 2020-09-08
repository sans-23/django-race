from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Question, Quiz

# Create your views here.

def quiz_list(request):
    quizes = Quiz.objects.all()
    return render(request, 'quiz/quizes.html', {'quizes': quizes})

def question_list(request, slug):
    questions = Question.objects.all()
    return render(request, 'quiz/questions.html', {'questions': questions, 'slug':slug})

def result_page(request, slug):
    if request.method == 'POST':
        response = request.POST
    else:
        response = "Fuck! You haven't tried yet"
    return render(request, 'quiz/result.html', {'response': response})
