from django.shortcuts import render

# Create your views here.

def dummy(request):
    ctx = 'Hola Brother'
    return render(request, 'leaderboard/dum.html', {'ctx':ctx})
