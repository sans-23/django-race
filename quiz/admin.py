from django.contrib import admin
from .models import Question, Quiz, Report, QuizAdmin, ReportAdmin

# Register your models here.
admin.site.register(Question)
admin.site.register(Report, ReportAdmin)
admin.site.register(Quiz, QuizAdmin)
