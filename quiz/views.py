from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Question, Quiz
from django.contrib.auth.decorators import login_required

# Create your views here.

def quiz_list(request):
    quizes = Quiz.objects.all()
    return render(request, 'quiz/quizes.html', {'quizes': quizes})

@login_required(login_url='/accounts/login/')
def question_list(request, slug):
    quiz = Quiz.objects.filter(slug=str(slug))[0:1]
    questions = Question.objects.filter(quiz=quiz)
    if request.method == 'POST':
        #calculating marks
        score = 0
        for question in questions:
            id = str(question.id)
            if( request.POST.get(id) == question.answer):
                score += question.marks
            else:
                score += question.negative

        request.session['response'] = request.POST
        request.session[slug] = score
        return redirect('quiz:result', slug=slug)

    else:
        return render(request, 'quiz/questions.html', {'questions': questions, 'slug':slug})

def result_page(request, slug):
    questions = Question.objects.all()
    score=request.session[slug]
    response = request.session['response']
    return render(request, 'quiz/result.html', {'questions': questions, 'score': score , 'response': response})
