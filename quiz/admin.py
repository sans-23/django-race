from django.contrib import admin
from .models import Question, Quiz, Report

# Register your models here.
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Report)
