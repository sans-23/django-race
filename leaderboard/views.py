from django.shortcuts import render
from quiz.models import Quiz, Question, Report, Response

# Create your views here.

def my_attempts(request):
    reports = Report.objects.filter(student=request.user)
    return render(request, 'leaderboard/attempts.html', {'reports':reports})

def report_card(request, slug):
    quiz = Quiz.objects.filter(slug=slug)[0]
    reports = Report.objects.filter(quiz=quiz)
    return render(request, 'leaderboard/reportcard.html', {'reports':reports, 'slug':slug})
