from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Quiz(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, blank=True, null=True)
    question = models.TextField()
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    diagram = models.ImageField(blank=True)
    marks = models.IntegerField(default=0)
    negative = models.IntegerField(default=0)

    def __str__(self):
        return self.question

# class GradeSheet(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,)
#     quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True,)
#     score = models.IntegerField(default=0)
