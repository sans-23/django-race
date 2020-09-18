from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Question, Quiz, Report, Response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.models import User


# Create your views here.

def quiz_list(request):
    quizes = Quiz.objects.all()
    return render(request, 'quiz/quizes.html', {'quizes': quizes})

@login_required(login_url='/accounts/login/')
def question_list(request, slug):
    quiz = Quiz.objects.filter(slug=str(slug))[0]
    questions = Question.objects.filter(quiz=quiz)
    return render(request, 'quiz/questions.html', {'questions': questions, 'slug':slug, 'quiz':quiz})

@login_required(login_url='/accounts/login/')
def response_page(request, slug, userid):
    quiz = Quiz.objects.filter(slug=slug)[0]
    user = User.objects.filter(id=userid)[0]
    response = Response.objects.filter(quiz=quiz, student=user)
    return render(request, 'quiz/records.html', {'response' : response})


@login_required(login_url='/accounts/login/')
def exam_view(request, slug):
    quiz = Quiz.objects.filter(slug=str(slug))[0]
    questions = Question.objects.filter(quiz=quiz)
    if request.method == 'POST':
        #calculating marks
        score = 0
        for question in questions:
            id = str(question.id)
            if( request.POST.get(id) == question.answer):
                score += question.marks
                try:
                    response = Response(quiz=quiz, student=request.user, question=question, is_correct=True, answer=request.POST.get(id))
                    response.save()
                except:
                    response = Response.objects.filter(quiz=quiz, question=question, student=request.user)[0]
                    attempt = response.attempt + 1
                    response_another = Response(quiz=quiz, student=request.user, question=question, is_correct=True, answer=request.POST.get(id), attempt=attempt)
                    response_another.save()
            else:
                score += question.negative
                try:
                    response = Response(quiz=quiz, student=request.user, question=question, is_correct=False, answer=request.POST.get(id))
                    response.save()
                except:
                    response = Response.objects.filter(quiz=quiz, question=question, student=request.user)[0]
                    attempt = response.attempt + 1
                    response_another = Response(quiz=quiz, student=request.user, question=question, is_correct=False, answer=request.POST.get(id), attempt=attempt)
                    response_another.save()
        try:
            report = Report(quiz=quiz, student=request.user, score=score)
            report.save()
        except:
            report = Report.objects.filter(quiz=quiz, student=request.user)[0]
            report.score=score
            report.attempt+=1
            report.save()

        return redirect('quiz:result', slug=slug)

    else:
        return render(request, 'quiz/exam.html', {'questions': questions, 'slug':slug})

@login_required(login_url='/accounts/login/')
def result_page(request, slug):
    quiz = Quiz.objects.filter(slug=str(slug))[0]
    report = Report.objects.filter(quiz=quiz, student=request.user)[0]
    return render(request, 'quiz/result.html', {'report': report})

@login_required(login_url='/accounts/login/')
def MyQuiz(request):
    quizes = Quiz.objects.filter(author=request.user)
    return render(request, 'quiz/myquiz.html', {'quizes': quizes})

class QuizCreate(LoginRequiredMixin, CreateView):
    model = Quiz
    fields = ['title', 'slug']
    success_url = reverse_lazy('quiz:my_quiz')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class QuestionCreate(LoginRequiredMixin, CreateView):
    model = Question
    fields = ['question', 'option1', 'option2', 'option3', 'option4', 'answer', 'marks', 'negative']
    success_url = reverse_lazy('quiz:my_quiz')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs['slug']
        quiz = Quiz.objects.filter(slug=slug)[0]
        context["quiz"] = quiz
        return context

    def form_valid(self, form):
        slug = self.kwargs['slug']
        quiz = Quiz.objects.filter(slug=slug)[0]
        form.instance.quiz = quiz
        return super().form_valid(form)


class QuestionUpdate(LoginRequiredMixin, UpdateView):
    model = Question
    fields = ['question', 'option1', 'option2', 'option3', 'option4', 'answer', 'marks', 'negative']
    success_url = reverse_lazy('quiz:quiz_list')

    template_name_suffix= '_update_form'


class QuestionDelete(LoginRequiredMixin, DeleteView):
    model = Question
    fields = '__all__'
    success_url = reverse_lazy('quiz:quiz_list')
