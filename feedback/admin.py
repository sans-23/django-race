from django.contrib import admin
from .models import Feedback, FeedbackAdmin

# Register your models here.
admin.site.register(Feedback,FeedbackAdmin)
