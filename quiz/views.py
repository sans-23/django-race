from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Question, Quiz
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import View


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
    quiz = Quiz.objects.filter(slug=str(slug))[0:1]
    questions = Question.objects.filter(quiz=quiz)
    score=request.session[slug]
    response = request.session['response']
    return render(request, 'quiz/result.html', {'questions': questions, 'score': score , 'response': response})

def MyQuiz(request):
    quizes = Quiz.objects.filter(author=request.user)
    return render(request, 'quiz/myquiz.html', {'quizes': quizes})

class QuizCreate(LoginRequiredMixin, CreateView):
    model = Quiz
    fields = ['title', 'slug']
    success_url = reverse_lazy('quiz:quiz_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class QuestionCreate(LoginRequiredMixin, CreateView):
    model = Question
    fields = ['question', 'option1', 'option2', 'option3', 'option4', 'answer', 'diagram', 'marks', 'negative']
    success_url = reverse_lazy('quiz:quiz_list')
    # slug = 'lorem-ipsum'
    #
    # quiz = Quiz.objects.filter(slug=slug)[0]

    def form_valid(self, form):
        slug = self.kwargs['slug']
        quiz = Quiz.objects.filter(slug=slug)[0]
        form.instance.quiz = quiz
        return super().form_valid(form)


class QuestionUpdate(LoginRequiredMixin, UpdateView):
    model = Question
    fields = '__all__'
    success_url = reverse_lazy('quiz:quiz_list')


class QuestionDelete(LoginRequiredMixin, DeleteView):
    model = Question
    fields = '__all__'
    success_url = reverse_lazy('quiz:quiz_list')
